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

class Constants(BaseConstants):
    name_in_url = "Questionnaire"
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

def random_initial():
    return random.uniform(0,100)


class Player(BasePlayer):
    Q1 = models.BooleanField(
        blank=True,
        choices=[[True, "Yes"], [False, "No"]],
        widget=widgets.RadioSelectHorizontal,
        label="Q1",
    )

    Q2 = models.IntegerField(
        blank=True,
        choices=[[1, "A"], 
                 [2, "B"], 
                 [3, "C"]],
        label="Q2",
        widget=widgets.RadioSelect,
    )

    Q3 = models.IntegerField(
        blank=True,
        choices=[[1, "A"],
                 [2, "B"],
                 [3, "C"],
                 [4, "D"]],
        label="Q3",
    )

    Q4 = models.FloatField(
        widget=widgets.Slider(show_value=True, attrs={'step': '1'}),
        max=100, min=0, blank=True, initial=random_initial(),
        label="Q4"
    )

    Q5 = models.IntegerField(label="Q5", max=100, min=0, blank=True)

    Q6 = models.FloatField(label="Q6", max=100, min=0, blank=True)

    Q7 = models.StringField(label="Q7", blank=True)

    Q8 = models.CurrencyField(
        label="Q8",
        blank=True
    )

    Q9 = models.LongStringField (
        label="Q9",
        blank=True,
    )

    Q10 = models.TextField(
        label="Q10",
        blank=True,
    )
    
