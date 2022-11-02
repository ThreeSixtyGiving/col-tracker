from random import choice

from dash import html

from ..settings import THREESIXTY_COLOURS
from ._utils import card_wrapper


def wordcloud(words, func="bigrams"):

    words = words.loc[words["func"] == func, "ngram"].value_counts()

    if not len(words):
        return None
    maxcount = words.max()
    scaling = 36 / maxcount

    spans = []
    colour = None
    for k, w in enumerate(words.head(30).items()):
        word, wordcount = w
        colour = choice([c for c in THREESIXTY_COLOURS if c != colour])
        spans.append(
            html.Span(
                children=word,
                style={
                    "fontSize": max(wordcount * scaling, 16),
                    "color": colour,
                    "marginRight": "20px",
                    "display": "inline-block",
                },
            )
        )
        # spans.append(' ')

    return card_wrapper(
        "Commonly used words",
        [
            html.P(className="align-left", children=spans),
        ],
        colour="yellow",
    )
