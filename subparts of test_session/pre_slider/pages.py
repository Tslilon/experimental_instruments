from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class pre_task_Q(Page):
    form_model = 'player'
    form_fields = ['self_rating']


page_sequence = [pre_task_Q]
