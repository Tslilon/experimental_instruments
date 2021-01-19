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

def make_field(label):
    return models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )


class Constants(BaseConstants):
    name_in_url = "Risk_Questionnaire"
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    risk_taking = models.IntegerField(
        widget=widgets.RadioSelect,
        label="",
        choices=[[0, "0 - Not willing at all to take risks"],
                 [1, "1"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4"],
                 [5, "5"],
                 [6, "6"],
                 [7, "7"],
                 [8, "8"],
                 [9, "9"],
                 [10, "10 - Very willing to take risks"]]
    )

    risk_car = make_field("while driving a car:")
    risk_money = make_field("regarding money:")
    risk_sport = make_field("in sport activities:")
    risk_career = make_field("regarding your career prospects:")
    risk_health = make_field("with your physical health:")
    risk_sex = make_field("in sexual activity (such as insisting on protected intecourse):")
    risk_crime = make_field("being in areas associated with higher crime rates or in the presence of people that you believe could be involved in criminal behaviour:")
    risk_drugs = make_field("using alcohol and/or drugs:")

    risk_investment_1 = models.IntegerField(
        label="Choose how much of your lottery earnings you want to put into this investment:",
        widget=widgets.RadioSelect,
        choices=[[0, "Nothing"],
                 [1, "An amount of 2,000 dollars"],
                 [2, "An amount of 4,000 dollars"],
                 [3, "An amount of 6,000 dollars"],
                 [4, "An amount of 8,000 dollars"],
                 [5, "The entire amount of 10,000 dollars"]],
        blank=True,
    )
    risk_investment_2 = models.IntegerField(
        label="Choose how much of your lottery earnings you want to put into this investment:",
        widget=widgets.RadioSelect,
        choices=[[5, "The entire amount of 10,000 dollars"],
                 [4, "An amount of 8,000 dollars"],
                 [3, "An amount of 6,000 dollars"],
                 [2, "An amount of 4,000 dollars"],
                 [1, "An amount of 2,000 dollars"],
                 [0, "Nothing"]],
        blank=True,
    )