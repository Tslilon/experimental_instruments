from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.MyPage)
        yield (pages.Results)


import csv

with open('ravens_first/Answers.csv') as matrix_file:
    matrices = list(csv.DictReader(matrix_file))

len(matrices)