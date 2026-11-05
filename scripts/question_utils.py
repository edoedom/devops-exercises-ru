"""Разбор учебных вопросов. Все пути вычисляются от каталога репозитория."""
from pathlib import Path
from random import choice
from typing import List
import re

ROOT = Path(__file__).resolve().parent.parent
README_PATH = ROOT / "README.md"
EXERCISES_PATH = ROOT / "exercises"
DETAILS_PATTERN = re.compile(r"<details(?:\s[^>]*)?>(.*?)</details>", re.DOTALL)
SUMMARY_PATTERN = re.compile(r"<summary>(.*?)</summary>", re.DOTALL)


def _text(value):
    if isinstance(value, str):
        return value
    if isinstance(value, bytes):
        return value.decode("utf-8")
    return "\n".join(_text(line) for line in value)


def get_file_content() -> str:
    return README_PATH.read_text(encoding="utf-8")


def get_question_answers(file_content):
    """Возвращает пары HTML-вопрос/HTML-ответ, без требования обёртки <b>."""
    pairs = []
    for detail in DETAILS_PATTERN.findall(_text(file_content)):
        summary = SUMMARY_PATTERN.search(detail)
        if summary:
            answer = detail[summary.end():].strip()
            answer = re.sub(r"^(?:\s*<br\s*/?>|\s*<b>)+", "", answer)
            answer = re.sub(r"</b>\s*$", "", answer).strip()
            pairs.append((summary.group(1).strip(), answer))
    return pairs


def get_question_list(file_content) -> List[str]:
    return [question for question, _ in get_question_answers(file_content)]


def has_answer(answer):
    return bool(re.sub(r"<[^>]+>|\s", "", answer) or re.search(r"<img\b", answer))


def get_answered_questions(file_content) -> List[str]:
    return [q for q, a in get_question_answers(file_content) if q and has_answer(a)]


def get_answers_count() -> List[int]:
    text = get_file_content()
    return [len(get_answered_questions(text)), len(get_question_list(text))]


def content_paths():
    # Материалы сертификаций повторяют разделы и не входят в этот счётчик.
    return [README_PATH] + sorted(
        p for p in (ROOT / "topics").rglob("README.md") if "exercises" not in p.parts
    )


def get_challenges_count() -> int:
    targets = set()
    pattern = re.compile(r"\[(?:Exercise|Задание)\]\(([^)#]+)(?:#[^)]*)?\)")
    for path in content_paths():
        for link in pattern.findall(path.read_text(encoding="utf-8")):
            if not re.match(r"\w+://", link):
                targets.add((path.parent / link).resolve())
    return len(targets)


def get_total_counts():
    return sum(len(get_question_list(p.read_text(encoding="utf-8")))
               for p in content_paths()), get_challenges_count()


def get_random_question(question_list, with_answer=False) -> str:
    candidates = list(question_list)
    if with_answer:
        answered = set(get_answered_questions(get_file_content()))
        candidates = [q for q in candidates if q in answered]
    if not candidates:
        raise ValueError("Нет подходящих вопросов")
    return choice(candidates)
