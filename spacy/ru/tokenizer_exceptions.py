# encoding: utf8
from __future__ import unicode_literals

from ..symbols import *


EXCEPTIONS = {}


DAYS_OF_WEEK = {
    'Пн.': [
        {ORTH: 'Пн.', LEMMA: 'Понедельник'}
    ],
    'Вт.': [
        {ORTH: 'Вт.', LEMMA: 'Вторник'}
    ],
    'Ср.': [
        {ORTH: 'Ср.', LEMMA: 'Среда'}
    ],
    'Чт.': [
        {ORTH: 'Чт.', LEMMA: 'Четверг'}
    ],
    'Пт.': [
        {ORTH: 'Пт.', LEMMA: 'Пятница'}
    ],
    'Сб.': [
        {ORTH: 'Сб.', LEMMA: 'Суббота'}
    ],
    'Вс.': [
        {ORTH: 'Вс.', LEMMA: 'Воскресенье'}
    ],
}


SHORTENIGS = {
    'т.п.': [
        {ORTH: 'т.', LEMMA: 'тому'},
        {ORTH: 'п.', LEMMA: 'подобное'}
    ],
    'т.д.': [
        {ORTH: 'т.', LEMMA: 'так'},
        {ORTH: 'д.', LEMMA: 'далее'}
    ],
    'т.о.': [
        {ORTH: 'т.', LEMMA: 'таким'},
        {ORTH: 'о.', LEMMA: 'образом'}
    ],
}


OTHER = {
    '\n': [
        {ORTH: '\n'}
    ],
    '\t': [
        {ORTH: '\t'}
    ]
}


TOKENIZER_EXCEPTIONS = dict(EXCEPTIONS)
TOKENIZER_EXCEPTIONS.update(DAYS_OF_WEEK)
TOKENIZER_EXCEPTIONS.update(SHORTENIGS)
TOKENIZER_EXCEPTIONS.update(OTHER)
