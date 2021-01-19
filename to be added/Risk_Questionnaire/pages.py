from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Risk_Q_1(Page):
    form_model = "player"
    form_fields = ["risk_taking"]


class Risk_Q_2(Page):
    form_model = "player"
    form_fields = ["risk_car", "risk_money", "risk_sport", "risk_career", "risk_health", "risk_strangers", "risk_sex", "risk_crime", "risk_drugs"]


class Risk_Q_3(Page):
    form_model = "player"
    form_fields = ["risk_investment_1", "risk_investment_2"]

# a way to randomize order of choices
#    def risk_investment_choices(self):
#        options=['X', 'Y']
#        random.shuffle(options)
#        return options


page_sequence = [Risk_Q_1, Risk_Q_2, Risk_Q_3]
