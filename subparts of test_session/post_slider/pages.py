from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class post_task_Q(Page):
    form_model = 'player'
    form_fields = ['self_rating']


page_sequence = [post_task_Q]
