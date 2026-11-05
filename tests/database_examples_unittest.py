from pathlib import Path
import re
import sqlite3
import unittest

from scripts.question_utils import get_question_answers

ROOT = Path(__file__).resolve().parent.parent


class MessageBoard(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(':memory:')
        self.db.executescript((ROOT / 'topics/databases/examples/message_board/schema.sql').read_text())
        self.assertEqual(self.db.execute('PRAGMA foreign_keys').fetchone()[0], 1)
        self.db.executescript('''
          INSERT INTO users(id, display_name) VALUES (1,'A'), (2,'B'), (3,'Outsider');
          INSERT INTO boards VALUES (10,'Main'), (20,'Other');
          INSERT INTO board_members(board_id,user_id) VALUES (10,1),(10,2),(20,1);
          INSERT INTO messages(id,board_id,author_id,body) VALUES (1,10,1,'Root'), (3,20,1,'Other root');
          INSERT INTO messages(id,board_id,author_id,reply_to_id,body) VALUES (2,10,2,1,'Reply');
          INSERT INTO categories(id,board_id,name) VALUES (1,10,'Release'), (2,20,'Release');
        ''')
        self.db.execute("UPDATE messages SET created_at='2020-01-01T00:00:00.000Z'")
        self.db.commit()

    def tearDown(self):
        self.db.close()

    def test_valid_reply_mentions_categories_and_edit(self):
        self.db.execute('INSERT INTO message_mentions VALUES (1,2,10)')
        self.db.execute('INSERT INTO message_categories VALUES (1,1,10)')
        self.db.execute('UPDATE messages SET body=? WHERE id=2', ('Edited reply',))
        self.assertEqual(self.db.execute('SELECT reply_to_id,body FROM messages WHERE id=2').fetchone(),
                         (1,'Edited reply'))
        self.assertEqual(self.db.execute('PRAGMA foreign_key_check').fetchall(), [])

    def test_nonmember_cannot_be_referenced_as_author(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.execute("INSERT INTO messages(board_id,author_id,body) VALUES (10,3,'No')")

    def test_reply_cannot_cross_boards(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.execute("INSERT INTO messages(board_id,author_id,reply_to_id,body) VALUES (10,1,3,'No')")

    def test_self_reply_and_parent_changes_are_rejected(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.execute("INSERT INTO messages(id,board_id,author_id,reply_to_id,body) VALUES (99,10,1,99,'No')")
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.execute('UPDATE messages SET reply_to_id=2 WHERE id=1')

    def test_category_cannot_cross_boards(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.execute('INSERT INTO message_categories VALUES (1,2,10)')

    def test_mentions_and_views_require_membership_in_that_board(self):
        for query in ['INSERT INTO message_mentions VALUES (1,3,10)',
                      "INSERT INTO message_views VALUES (1,3,10,'2026-11-05T10:00:00.000Z')"]:
            with self.subTest(query=query), self.assertRaises(sqlite3.IntegrityError):
                self.db.execute(query)

    def test_distinct_view_times_are_kept_but_duplicate_event_is_not(self):
        self.db.execute("INSERT INTO message_views VALUES (1,2,10,'2026-11-05T10:00:00.000Z')")
        self.db.execute("INSERT INTO message_views VALUES (1,2,10,'2026-11-05T10:01:00.000Z')")
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.execute("INSERT INTO message_views VALUES (1,2,10,'2026-11-05T10:00:00.000Z')")
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM message_views').fetchone()[0], 2)

    def test_parent_deletion_does_not_orphan_replies(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.execute('DELETE FROM messages WHERE id=1')

    def test_blank_body_and_duplicate_category_name_are_rejected(self):
        for query in ["INSERT INTO messages(board_id,author_id,body) VALUES (10,1,'  ')",
                      "INSERT INTO categories(board_id,name) VALUES (10,'Release')"]:
            with self.subTest(query=query), self.assertRaises(sqlite3.IntegrityError):
                self.db.execute(query)

    def test_keyset_pages_with_equal_timestamps_do_not_repeat_rows(self):
        stamp = '2026-11-05T10:00:00.000Z'
        for mid in [10,11,12,13]:
            self.db.execute('INSERT INTO messages(id,board_id,author_id,body,created_at) VALUES (?,10,1,?,?)',
                            (mid,str(mid),stamp))
        query = (ROOT/'topics/databases/examples/message_board/page.sql').read_text()
        first = self.db.execute(query,(10,'9999-12-31T00:00:00.000Z',9999,2)).fetchall()
        self.assertEqual([row[0] for row in first],[13,12])
        second = self.db.execute(query,(10,first[-1][1],first[-1][0],2)).fetchall()
        self.assertEqual([row[0] for row in second],[11,10])
        self.assertFalse({row[0] for row in first} & {row[0] for row in second})

    def test_check_null_and_left_join_filter_semantics(self):
        self.db.executescript('CREATE TABLE samples(value INTEGER CHECK(value > 0));'
                              'INSERT INTO samples VALUES(NULL),(1);'
                              'CREATE TABLE a(id INTEGER PRIMARY KEY);'
                              'CREATE TABLE b(id INTEGER, flag INTEGER);'
                              'INSERT INTO a VALUES(1),(2); INSERT INTO b VALUES(1,0);')
        self.assertEqual(self.db.execute('SELECT COUNT(*),COUNT(value) FROM samples').fetchone(),(2,1))
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM samples WHERE value = NULL').fetchone()[0],0)
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM samples WHERE value IS NULL').fetchone()[0],1)
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.execute('INSERT INTO samples VALUES(0)')
        self.assertEqual(self.db.execute('SELECT a.id,b.id FROM a LEFT JOIN b ON a.id=b.id AND b.flag=1').fetchall(),
                         [(1,None),(2,None)])
        self.assertEqual(self.db.execute('SELECT a.id,b.id FROM a LEFT JOIN b ON a.id=b.id WHERE b.flag=1').fetchall(),[])


class DocumentedQueries(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(':memory:')
        self.db.executescript('''
            CREATE TABLE Customers(Customer_ID INTEGER PRIMARY KEY, Customer_Name TEXT, Items_in_cart INTEGER, Cash_spent_to_Date NUMERIC);
            CREATE TABLE Orders(Customer_ID INTEGER, Order_ID TEXT, Item TEXT, Price NUMERIC, Date_sold TEXT);
            INSERT INTO Customers VALUES (100204,'John Smith',0,20.00), (100205,'Jane Smith',3,40.00),
              (100206,'Bobby Frank',1,100.20), (100207,'No Orders',0,0);
            INSERT INTO Orders VALUES
              (100206,'A123','Rubber Ducky',2.20,'2019-09-18'),
              (100206,'A123','Bubble Bath',8.00,'2019-09-18'),
              (100206,'Q987','80-Pack TP',90.00,'2019-09-20'),
              (100205,'Z001','Cat Food - Tuna Fish',10.00,'2019-08-05'),
              (100205,'Z001','Cat Food - Chicken',10.00,'2019-08-05'),
              (100205,'Z001','Cat Food - Beef',10.00,'2019-08-05'),
              (100205,'Z001','Cat Food - Kitty quesadilla',10.00,'2019-08-05'),
              (100204,'X202','Coffee',20.00,'2019-04-29');
        ''')
        self.answers = dict(get_question_answers((ROOT / 'README.md').read_text()))

    def tearDown(self):
        self.db.close()

    def query(self, question):
        match = re.search(r'```sql\n(.*?)```', self.answers[question], re.S)
        self.assertIsNotNone(match, question)
        return self.db.execute(match[1]).fetchall()

    def test_basic_queries_are_executed_from_the_readme(self):
        self.assertEqual(len(self.query('Как выбрать все поля таблицы?')),4)
        self.assertEqual(self.query('Сколько товаров в корзине John Smith?'),[(0,)])
        self.assertAlmostEqual(self.query('Какова общая сумма расходов всех покупателей?')[0][0],160.2)
        self.assertEqual(self.query('У скольких покупателей корзина непустая?'),[(2,)])

    def test_join_keeps_customer_without_orders(self):
        rows = self.query('Как показать, кто какие товары заказал?')
        self.assertIn(('No Orders', None), rows)
        self.assertEqual(len(rows),9)

    def test_cte_aggregates_each_customer_once(self):
        self.assertEqual(self.query('Как с помощью WITH показать покупателей кошачьего корма и сумму их покупок корма?'),
                         [('Jane Smith',40)])

    def test_year_range_handles_last_day_next_year_and_null(self):
        self.db.execute('CREATE TABLE shawarma_purchases(purchased_at TEXT)')
        values = ['2016-12-31T23:59:59.999Z','2017-01-01T00:00:00.000Z',
                  '2017-12-31T00:00:00.000Z','2017-12-31T23:59:59.999Z',
                  '2018-01-01T00:00:00.000Z',None]
        self.db.executemany('INSERT INTO shawarma_purchases VALUES (?)',[(x,) for x in values])
        query = (ROOT/'topics/sql/examples/date_range/query.sql').read_text()
        self.assertEqual(self.db.execute(query).fetchone()[0],3)
