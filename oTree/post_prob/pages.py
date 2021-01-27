from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class post_info_Q(Page):

        form_model = 'player'
        form_fields = ['probability']

        def is_displayed(self):
                return random.randint(0, 1) == 1


page_sequence = [post_info_Q]
