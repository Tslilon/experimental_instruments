from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class pre_info_Q(Page):
    form_model = 'player'
    form_fields = ['probability']


page_sequence = [pre_info_Q]
