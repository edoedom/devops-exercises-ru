"""Обновление строки :bar_chart:; --check проверяет число без записи."""
import argparse
import re
from question_utils import README_PATH, get_total_counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    questions, exercises = get_total_counts()
    total = questions + exercises
    text = README_PATH.read_text(encoding="utf-8")
    pattern = r"(?m)^:bar_chart:[^\n]*$"
    replacement = (f":bar_chart: &nbsp;**{total}** вопросов и упражнений "
                   f"({questions} вопросов, {exercises} ссылок на уникальные задания "
                   "в основном README и README разделов; без повторов сертификаций).")
    new, count = re.subn(pattern, lambda _: replacement, text)
    if count != 1:
        raise SystemExit("Ожидалась одна строка :bar_chart:")
    print(replacement)
    if args.check:
        if new != text:
            raise SystemExit("Счётчик устарел; запустите scripts/update_question_number.py")
    else:
        README_PATH.write_text(new, encoding="utf-8")


if __name__ == "__main__":
    main()
