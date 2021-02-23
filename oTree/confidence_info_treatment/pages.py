from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

import sys
sys.path.append("../settings")
from settings import RANDOMIZATION


class post_info_Q(Page):

        form_model = 'player'
        form_fields = ['probability']

        def is_displayed(self):
        	if RANDOMIZATION == True:
        		return self.participant.vars['treatment'] == "with_info"
        	else:
        		return self.session.config['treatment'] == "with_info"


page_sequence = [post_info_Q]
