# encoding: utf8
from __future__ import unicode_literals

from ..language_data.punctuation import LIST_CURRENCY, LIST_ELLIPSES, \
    LIST_PUNCT, LIST_QUOTES


TOKENIZER_SUFFIXES = (LIST_CURRENCY + LIST_ELLIPSES + LIST_PUNCT + LIST_QUOTES)


__all__ = ["TOKENIZER_SUFFIXES"]
