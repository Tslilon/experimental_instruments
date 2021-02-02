from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Q_Introduction(Page):
    pass


class Page_1(Page):
    form_model = "player"
    form_fields = ['Q1', 'Q2', 'Q3', 'Q4']


class Page_2(Page):
    form_model = "player"
    form_fields = ['Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10']


page_sequence = [Page_1, Page_2]
