from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import random


class PlayerBot(Bot):

    def play_round(self):
        a = (random.randint(0, 1) == 1)
        if self.round_number == 1:
            yield (pages.Instructions)
        yield (pages.Time_Preference, {'decision': a})
