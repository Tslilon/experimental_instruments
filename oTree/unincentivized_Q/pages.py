from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Intro(Page):
    form_model = "player"
    form_fields = ['consent']


class Verification(Page):
    form_model = "player"
    form_fields = ['email']


class Demographics(Page):
    form_model = "player"
    form_fields = ['age', 'gender', 'gender_other', 'marital', 'children', 'location', 'religion', 'religion_other', 'education', 'household']


page_sequence = [Intro, Verification, Demographics]
