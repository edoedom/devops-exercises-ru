<a id="database-table-for-message-board-system"></a>
## Таблица базы данных для системы обмена сообщениями

<a id="instructions"></a>
### Инструкции

Спроектируйте таблицу базы данных для системы обмена сообщениями. Она должна учитывать:

* Персональные данные.
* Кто и когда просмотрел сообщение.
* Ответы.
* Людей, отмеченных в сообщении.
* Категории сообщений.

Примечания:

* Писать SQL не требуется.
* Укажите названия таблиц и полей, типы данных и используемые внешние ключи.

<a id="solution"></a>
### Решение

Примечание: это один из возможных вариантов структуры.

PK — первичный ключ; FK — внешний ключ. Названия таблиц, полей и типы данных сохранены из исходной схемы.

                                ----- People -----
                                ID int PK
                                FirstName varchar(255)
                                LastName varchar(255)
                                DOB date
                                Gender varchar(1)
                                Phone varchar(10)

                                       |               \
                                       |                \ 
                                       |                 \
                                       v                  \ 
                                                           \
                                --- Messages ---            v
                                ID int PK
                                MessageBoardID FK             --- MessageTags ---
--- MessageBoards ---           PeopleID int FK               ID int PK
ID int PK              ---->    MsgDate datetime       --->   MessageID FK
Board text                      Message text                  PeopleID int Fk
                                MessageID (FK)
                                       ^      |
                                       |      |
                                       |______|
