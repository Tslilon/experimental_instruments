from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import math

author = 'Your name here'

doc = """
Your app description
"""

class Constants(BaseConstants):
    name_in_url = 'Time_Preference'
    players_per_group = None
    num_rounds = 5
    start_diff = 1
    start_high = 15
    start_low = 7
    future_date = "in two weeks"
    progress_bar = True

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.BooleanField()
    high = models.FloatField()
    low = models.FloatField()
    solution = models.FloatField()
    payoff_now = models.FloatField()
    payoff_later = models.FloatField()
    time_spend = models.FloatField()
    payoff_timing = models.StringField()

    def role(self):
        if self.participant.label == "Admin":
            return "Admin"
        else:
            return "Player"

    def show(self):
        if self.participant.label == "Admin":
            return 0
        else:
            return 1

    def round(self):
        return self.round_number

    def L(self):
        self.low = Constants.start_low
        return self.low

    def R(self):
        if self.round_number == 1:
            self.high = Constants.start_high
            self.low = Constants.start_low
        else:
            if self.in_round(self.round_number-1).decision == 0:
                self.high = self.in_round(self.round_number-1).high + float(Constants.start_diff*math.pow(2,Constants.num_rounds-(self.round_number)))
                self.low = self.in_round(self.round_number-1).low
            else:
                self.high = self.in_round(self.round_number-1).high - float(Constants.start_diff*math.pow(2,Constants.num_rounds-(self.round_number)))
                self.low = self.in_round(self.round_number-1).low

        return round(self.high,2)

    def sol(self):
        if self.in_round(self.round_number).decision == 0:
            return self.in_round(self.round_number).high + float(Constants.start_diff*math.pow(2,Constants.num_rounds-(self.round_number)-1))
        else:
            return self.in_round(self.round_number).high - float(Constants.start_diff*math.pow(2,Constants.num_rounds-(self.round_number)-1))

    def set_payoff(self):
        self.solution = self.sol()

        if self.decision == 0:
            self.payoff_now = self.low
            self.payoff_later = 0

        else:
            self.payoff_now = 0
            self.payoff_later = self.high

