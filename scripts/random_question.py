"""Самопроверка по всем разделам или одной теме без подключения к сети."""
import argparse
from html.parser import HTMLParser
from random import Random

from markdown_it import MarkdownIt
from question_utils import content_paths, get_question_answers, has_answer


class PlainText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)

    def handle_starttag(self, tag, attrs):
        if tag in {'br', 'p', 'li', 'pre'}:
            self.parts.append('\n')
        if tag == 'img':
            self.parts.append('[изображение: ' + dict(attrs).get('src', '') + ']')

    def handle_endtag(self, tag):
        if tag in {'p', 'li', 'pre', 'h1', 'h2', 'h3'}:
            self.parts.append('\n')


def plain(text):
    parser = PlainText()
    parser.feed(MarkdownIt('commonmark').render(text))
    return ''.join(parser.parts).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--topic', default='all', help='all, main или имя темы: linux, gitops, sre…')
    parser.add_argument('--list-topics', action='store_true')
    parser.add_argument('-s', '--skip', action='store_true', help='пропускать вопросы без ответа')
    parser.add_argument('--once', action='store_true', help='показать один вопрос без ожидания ввода')
    parser.add_argument('--show-answer', action='store_true', help='сразу показать ответ')
    parser.add_argument('--seed', type=int, help='воспроизводимый выбор при том же содержимом')
    args = parser.parse_args()
    paths = content_paths()
    topics = {'main': [paths[0]]}
    for path in paths[1:]:
        # Не включаем технические README вложенных solutions в список учебных тем.
        if path.parent.parent.name == 'topics':
            topics.setdefault(path.parent.name, []).append(path)
    if args.list_topics:
        print('\n'.join(['all'] + sorted(topics)))
        return
    if args.topic != 'all' and args.topic not in topics:
        parser.error('Неизвестная тема; используйте --list-topics')
    selected = paths if args.topic == 'all' else topics[args.topic]
    pairs = [(q, a) for path in selected
             for q, a in get_question_answers(path.read_text(encoding='utf-8'))
             if q and (not args.skip or has_answer(a))]
    if not pairs:
        parser.error('В выбранной теме нет подходящих вопросов')
    random = Random(args.seed)
    try:
        while True:
            question, answer = random.choice(pairs)
            print(plain(question))
            if args.show_answer:
                print('\nОтвет:\n' + plain(answer))
            elif not args.once:
                input('Enter — показать ответ; Ctrl-C — выход ')
                print(plain(answer) or 'Ответ отсутствует')
            if args.once:
                break
            input('Enter — следующий вопрос ')
    except (KeyboardInterrupt, EOFError):
        print('\nДо встречи!')


if __name__ == '__main__':
    main()
