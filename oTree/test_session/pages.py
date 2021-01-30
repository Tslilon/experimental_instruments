from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random
import time

class pre_task_Q(Page):

    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'
    form_fields = ['self_rating1']

class StartPage(Page):
    def is_displayed(self):
        if self.round_number == 1:
            print('This is the start of Ravens tests')
        return self.round_number == 1 and (not self.session.config['debug'])


class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1

#    def before_next_page(self):
        # user has 10 minutes to complete as many pages as possible
        # self.participant.vars['expiry_timestamp'] = time.time() + Constants.minutes_given*60


class QuestionPage(Page):
    form_model = 'player'
    form_fields = ['answer']
    timeout_seconds = Constants.seconds_given


#   def get_timeout_seconds(self):
    #    return self.participant.vars['expiry_timestamp'] - time.time()


    def vars_for_template(self):
        if self.round_number == 1:
            self.participant.vars['Q_seq'] = list(range(1, 13))
            random.shuffle(self.participant.vars['Q_seq'])
        return {'image_path': 'ravens/{}.jpg'.format(self.participant.vars['Q_seq'][self.round_number - 1])}

    def before_next_page(self):
        if self.timeout_happened:
            self.player.answer = 0
        self.player.ans_correct = self.player.answer == Constants.answer_keys[self.round_number-1]
        self.player.participant.vars['payoff_ravens'] += self.player.ans_correct * Constants.payment_per_question
        if Constants.payment_in_points > 0:
            self.player.payoff = self.player.ans_correct*Constants.payment_in_points
        else:
            self.player.payoff = (self.player.ans_correct*Constants.payment_per_question /
                                  self.session.config['payment_per_right_raven']) # to measure in point


class Results(Page):

    def is_displayed(self):
        return False

    def vars_for_template(self):
        return {
            'total_correct': sum([p.ans_correct for p in self.player.in_all_rounds()]),
            'earnings': sum([p.ans_correct for p in self.player.in_all_rounds()])*Constants.payment_per_question,
                }

    def before_next_page(self):
        for p in self.subsession.get_players():
            p.participant.vars['payoff_ravens'] = (sum([p.ans_correct for p in self.player.in_all_rounds()]) *
                                                   Constants.payment_per_question)


class post_task_Q(Page):

    def is_displayed(self):
        return self.round_number == 12

    form_model = 'player'
    form_fields = ['self_rating2']

class pre_info_Q(Page):

    def is_displayed(self):
        return self.round_number == 12

    form_model = 'player'
    form_fields = ['probability']

page_sequence = [
    pre_task_Q,
    #StartPage,
    Introduction,
    QuestionPage,
    Results,
    post_task_Q,
    pre_info_Q
]
