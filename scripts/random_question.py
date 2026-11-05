"""Интерактивная самопроверка по главному README."""
import argparse
from random import choice
from question_utils import get_file_content, get_question_answers, has_answer


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-s", "--skip", action="store_true",
                        help="пропускать вопросы без ответа")
    args = parser.parse_args()
    pairs = [(q, a) for q, a in get_question_answers(get_file_content())
             if q and (not args.skip or has_answer(a))]
    if not pairs:
        raise SystemExit("Подходящих вопросов нет")
    try:
        while True:
            question, answer = choice(pairs)
            print(question)
            input("Enter — показать ответ; Ctrl-C — выход ")
            print(answer or "Ответ отсутствует")
            input("Enter — следующий вопрос ")
    except (KeyboardInterrupt, EOFError):
        print("\nДо встречи!")


if __name__ == "__main__":
    main()
