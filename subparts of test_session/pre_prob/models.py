from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random
from django.conf import settings

class Constants(BaseConstants):
    # oTree Constants
    name_in_url = "pre_prob"
    players_per_group = None
    num_rounds = 1

def random_initial():
    return random.uniform(0,100)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    probability = models.IntegerField(
        widget=widgets.Slider(show_value=True, attrs={'step': '1'}),
        max=100, min=0, blank=False, initial=random_initial(),
        label="What is the probability that you outperformed 90% of the participants in the previous task?"
    )