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
from django.conf import settings

import sys
sys.path.append("../translation")
from translation import translation_dict

sys.path.append("../settings")
from settings import LANGUAGE_CODE

class Constants(BaseConstants):
    # oTree Constants
    name_in_url = "confidence_info_treatment"
    players_per_group = None
    num_rounds = 1

    prob_title = translation_dict["post_info"]["title"][LANGUAGE_CODE]
    prob_instruction1 = translation_dict["post_info"]["instruction1"][LANGUAGE_CODE]
    prob_instruction2 = translation_dict["post_info"]["instruction2"][LANGUAGE_CODE]
    prob_left_label = translation_dict["post_info"]["left_label"][LANGUAGE_CODE]
    prob_right_label = translation_dict["post_info"]["right_label"][LANGUAGE_CODE]

def random_initial():
    return random.uniform(0,100)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    probability = models.FloatField(
        widget=widgets.Slider(show_value=True, attrs={'step': '1'}),
        max=100, min=0, blank=False, initial=random_initial(),
        label=translation_dict["pre_info"]["probability_Q"][LANGUAGE_CODE]
    )