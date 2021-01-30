from otree.api import (
    models, 
    widgets, 
    BaseConstants, 
    BaseSubsession, 
    BaseGroup, 
    BasePlayer,
    Currency as c, 
    currency_range
)
import random
from django.conf import settings


author = 'Huanren Zhang (for Ravens)'

doc = """
Raven's progressive matrices test measuring cognitive ability
"""


def minutes(num):
    if num/60 % 1 == 0:
        return int(num/60)
    else:
        return round(num/60,2)


class Constants(BaseConstants):
    name_in_url = 'test_session'
    players_per_group = None
    seconds_given = 120
    minutes_given = minutes(seconds_given)
#   minutes_given = 10
    payment_per_question = 1
    payment_in_points = 3
    num_rounds = 12
    answer_keys = [4, 2, 2, 1, 2, 7, 3, 5, 2, 5, 6, 4]
    instructions_template = 'ravens/Instructions.html'

def random_initial1():
    return random.uniform(0,10)

def random_initial2():
    return random.uniform(0,100)

class Subsession(BaseSubsession):
    def creating_session(self):
        # this is run before the start of every round
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['payoff_ravens'] = 0


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    self_rating1 = models.IntegerField(
        widget=widgets.Slider(show_value=True, attrs={'step': '1'}),
        max=10, min=0, blank=False, initial=random_initial1(),
        label="How well do you think you'll do in the task?"
    )
    answer = models.IntegerField(choices=[1,2,3,4,5,6,7,8],widget=widgets.RadioSelectHorizontal)
    ans_correct = models.BooleanField()
    self_rating2 = models.IntegerField(
        widget=widgets.Slider(show_value=True, attrs={'step': '1'}),
        max=10, min=0, blank=False, initial=random_initial1(),
        label="How well do you think you did in the task?"
    )
    probability = models.IntegerField(
        widget=widgets.Slider(show_value=True, attrs={'step': '1'}),
        max=100, min=0, blank=False, initial=random_initial2(),
        label="What is the probability that you outperformed 90% of the participants in the previous task?"
    )

