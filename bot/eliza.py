from typing import List, Tuple
import random
from .nlu import NLU

def is_in_sentence(*args: str) -> bool:
    sentence, *words = args
    return any(word for word in words if word in sentence)


def act_hello() -> str:
    return random.choice(
        [
            "Dzień dobry, witam w interaktywnej bibliotece",
            "Witam w interaktywnej biblitece",
            "Dzień dobry, w czym mogę pomóc?",
            "Witam w interaktywnej bibliotece książnicy płockiej, jak mogę pomóc?",
        ]
    )


def act_bye() -> str:
    return random.choice(
        ["Do zobaczenia", "Dziękuję i życzę miłej lektury", "Do widzenia"]
    )


def act_request(sentence: str, slots: List[Tuple[str, str]]) -> str:
    if is_in_sentence(sentence, "wypożyczyć", "interesuje", "wypożyczenie"):
        book = " ".join(slot[1] for slot in slots)
        return f"Książka {book} została dla Ciebie zapisana i czeka na odbiór"
    elif is_in_sentence(sentence, "oddać", "zwrócić"):
        return "Proszę przynieść książkę/i do naszej biblioteki"
    elif is_in_sentence(sentence, "rezerwacja", "zarezerwować", "rezerwacji"):
        if slots:
            book = " ".join(slot[1] for slot in slots)
            return f"Książka {book} została zarezerwowana"
        return "Niestety nie mamy tej książki"
    elif is_in_sentence(sentence, "biblioteka", "otwarta"):
        return "Biblioteka jest otwarta od poniedziałku do soboty w godzinach 8-20, bez świąt"
    elif is_in_sentence(sentence, "założyć kartę", "założyć konto", "założyć"):
        return """Założyć kartę biblioteczną można przez naszą stronę www.biblioteka.pl,
            karta przyjdzie pocztą a opłata to 5 zł."""
    elif is_in_sentence(
        sentence,
        "zgubiona",
        "zgubiłem kartę",
        "zgubiłam kartę",
        "zniszczyłem kartę",
        "zniszczyłam kartę",
    ):
        return "W razie zgubienia lub zniszczenia karty należy przyjść do biblioteki w celu jej zablokowania."
    return "Nie rozumiem pytania lub nie posiadamy takiej książki"


def act_thankyou() -> str:
    return random.choice(["Proszę!", "Nie ma za co", "Po to tutaj jestem!"])


def act_negate() -> str:
    return "Akcja została cofnięta"


def act_confirm(sentence: str, slots: List[Tuple[str, str]]) -> str:
    if slots:
        book = " ".join(slot[1] for slot in slots)
        if is_in_sentence(sentence, "wypożyczona"):
            return f"Książka {book} została wypożyczona"
        elif is_in_sentence(sentence, "zarezerwowana"):
            return f"Książka {book} została zarezerwowana"
    return "Nie rozumiem pytania lub nie posiadamy takiej książki"


def act_ack() -> str:
    return random.choice(["W czymś jeszcze mogę pomóc?", "Co mogę jeszcze zrobić"])


def answer(sentence: str, nlu: NLU) -> str:
    nlu_match = nlu.match(sentence)
    act, slots = nlu_match["act"], nlu_match["slots"]
    if act == "hello":
        return act_hello()
    elif act == "bye":
        return act_bye()
    elif act == "request":
        return act_request(sentence, slots)
    elif act == "thankyou":
        return act_thankyou()
    elif act == "negate":
        return act_negate()
    elif act == "confirm":
        return act_confirm(sentence, slots)
    elif act == "ack":
        return act_ack()
    return "Nie rozumiem pytania lub nie posiadamy takiej książki"