from otree.api import (
    models, 
    widgets, 
    BaseConstants, 
    BaseSubsession, 
    BaseGroup, 
    BasePlayer,
    Currency as c, 
    currency_range
)
import random
from django.conf import settings

import sys
sys.path.append("../translation")
from translation import translation_dict

sys.path.append("../settings")
from settings import LANGUAGE_CODE

author = 'Huanren Zhang (for Ravens)'

doc = """
Raven's progressive matrices test measuring cognitive ability
"""

def minutes(num):
    if num/60 % 1 == 0:
        return int(num/60)
    else:
        return round(num/60,2)


class Constants(BaseConstants):
    name_in_url = 'ravens'
    players_per_group = None
    seconds_given = 120
    minutes_given = minutes(seconds_given)
#   minutes_given = 10
    payment_per_question = 1
    payment_in_points = 3
    num_rounds = 12
    answer_keys = [4, 2, 2, 1, 2, 7, 3, 5, 2, 5, 6, 4]
    instructions_template = 'ravens/Instructions.html'

    pre_title = translation_dict["pre_slider"]["title"][LANGUAGE_CODE]
    pre_instruction1 = translation_dict["pre_slider"]["instruction1"][LANGUAGE_CODE]
    pre_instruction2 = translation_dict["pre_slider"]["instruction2"][LANGUAGE_CODE]
    pre_left_label = translation_dict["pre_slider"]["left_label"][LANGUAGE_CODE]
    pre_right_label = translation_dict["pre_slider"]["right_label"][LANGUAGE_CODE]

    raven_intro_title = translation_dict["raven_intro"]["title"][LANGUAGE_CODE]
    raven_intro_para_1 = translation_dict["raven_intro"]["paragraph_1"][LANGUAGE_CODE]
    raven_intro_para_2 = translation_dict["raven_intro"]["paragraph_2"][LANGUAGE_CODE]
    raven_intro_para_3 = translation_dict["raven_intro"]["paragraph_3"][LANGUAGE_CODE]
    raven_intro_para_4 = translation_dict["raven_intro"]["paragraph_4"][LANGUAGE_CODE]
    raven_intro_para_5 = translation_dict["raven_intro"]["paragraph_5"][LANGUAGE_CODE]
    raven_intro_para_6 = translation_dict["raven_intro"]["paragraph_6"][LANGUAGE_CODE]

    raven_question_title_part1 = translation_dict["raven_question"]["title_part1"][LANGUAGE_CODE]
    raven_question_title_part2 = translation_dict["raven_question"]["title_part2"][LANGUAGE_CODE]

    post_title = translation_dict["post_slider"]["title"][LANGUAGE_CODE]
    post_instruction = translation_dict["post_slider"]["instruction"][LANGUAGE_CODE]
    post_left_label = translation_dict["post_slider"]["left_label"][LANGUAGE_CODE]
    post_right_label = translation_dict["post_slider"]["right_label"][LANGUAGE_CODE]

    prob_title = translation_dict["pre_info"]["title"][LANGUAGE_CODE]
    prob_instruction = translation_dict["pre_info"]["instruction"][LANGUAGE_CODE]
    prob_left_label = translation_dict["pre_info"]["left_label"][LANGUAGE_CODE]
    prob_right_label = translation_dict["pre_info"]["right_label"][LANGUAGE_CODE]



def random_initial1():
    return random.uniform(0,10)

def random_initial2():
    return random.uniform(0,100)

class Subsession(BaseSubsession):
    def creating_session(self):
        # this is run before the start of every round
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['treatment'] = random.choice(["with_info", "without_info"])
                p.participant.vars['Q_seq'] = list(range(1, 13))
                p.participant.vars['payoff_ravens'] = 0


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    self_rating1 = models.IntegerField(
        widget=widgets.Slider(show_value=True, attrs={'step': '1'}),
        max=10, min=0, blank=False, initial=random_initial1(),
        label=translation_dict["pre_slider"]["self_rating_Q"][LANGUAGE_CODE]
    )
    answer = models.IntegerField(
        choices=[1,2,3,4,5,6,7,8],widget=widgets.RadioSelectHorizontal,
        label=translation_dict["raven_question"]["question"][LANGUAGE_CODE]
    )
    ans_correct = models.BooleanField()


    self_rating2 = models.IntegerField(
        widget=widgets.Slider(show_value=True, attrs={'step': '1'}),
        max=10, min=0, blank=False, initial=random_initial1(),
        label=translation_dict["post_slider"]["self_rating_Q"][LANGUAGE_CODE]
    )
    probability = models.IntegerField(
        widget=widgets.Slider(show_value=True, attrs={'step': '1'}),
        max=100, min=0, blank=False, initial=random_initial2(),
        label=translation_dict["pre_info"]["probability_Q"][LANGUAGE_CODE]
    )

