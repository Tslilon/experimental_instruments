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
    minutes = 0
    payment = 0


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

def random_initial():
    return random.uniform(0,100)


class Player(BasePlayer):
    consent = models.BooleanField(
        blank=True,
        choices=[[True, "Yes"], [False, "No"]],
        widget=widgets.RadioSelectHorizontal,
        label="Given all the information above, do you agree to participate in our labor market study?",
    )

    email = models.StringField(label="Email address:", blank=True)

    age = models.IntegerField(label="What is your age?", min=15, max=120, blank=True)

    gender = models.IntegerField(
        blank=True,
        choices=[[1, "Male"], 
                 [2, "Female"], 
                 [3, "Other"]],
        label="What is your gender?",
        widget=widgets.RadioSelect,
    )

    gender_other = models.StringField(
        label="If you picked \"Other\" , please speficify:",
        blank=True,
    )

    marital = models.IntegerField(
        blank=True,
        choices=[[1, "Single (never married)"], 
                 [2, "Married"], 
                 [3, "Separated"],
                 [4, "Divorced"],
                 [5, "Widowed"], 
                 [6, "Domestic partnership (living together but not married)"]],
        label="What is your marital status?",
        widget=widgets.RadioSelect,
    )

    children = models.IntegerField(label="How many children do you have?", min=0, max=20, blank=True)

    location = models.IntegerField(
        blank=True,
        choices=[[1, "location1"],
                 [2, "location2"],
                 [3, "location3"],
                 [4, "location4"]],
        label="Where do you live?",
    )

    religion = models.IntegerField(
        blank=True,
        choices=[[1, "Jewish"], 
                 [2, "Muslim"], 
                 [3, "Christian"],
                 [4, "Other"]],
        label="How do you identify?",
        widget=widgets.RadioSelect,
    )

    religion_other = models.StringField(
        label="If you picked \"Other\" , please speficify:",
        blank=True,
    )

    education = models.IntegerField(
        blank=True,
        choices=[[1, "Some high school or less"], 
                 [2, "High school diploma or equivalent"], 
                 [3, "Some college"],
                 [4, "College diploma"],
                 [5, "Some graduate school"], 
                 [6, "Graduate degree"]],
        label="What is the highest level of education you have completed?",
        widget=widgets.RadioSelect,
    )

    household = models.IntegerField(label="Including yourself, how many people live in your household?", min=0, max=50, blank=True)
    
