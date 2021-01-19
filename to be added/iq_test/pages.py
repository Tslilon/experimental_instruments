from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time
from math import floor
import pdb


class IQTest(Page):
    form_model = 'player'
    form_fields = ['hidden_answer']

    timer_text = 'Time left to complete the test:'

    def get_timeout_seconds(self):
        return self.participant.vars['remaining_time']

    def is_displayed(self):
        # Display the IQ test only if the participant while there is time left
        return self.participant.vars['remaining_time'] > 1

    def vars_for_template(self):
        num = self.round_number
        dem = Constants.num_rounds
        if self.round_number == 1:
            self.participant.vars['timestamps'] = [time.time()]
        return {
            'num': num,
            'dem': dem,

            'mat': 'raven/matrices_cleaned/{}/{}.JPG'.format(
                self.player.matrix_id, self.player.matrix_id),
            'mat_sol1': 'raven/matrices_cleaned/{}/{}_{}.JPG'.format(
                self.player.matrix_id, self.player.matrix_id, 1),
            'mat_sol2': 'raven/matrices_cleaned/{}/{}_{}.JPG'.format(
                self.player.matrix_id, self.player.matrix_id, 2),
            'mat_sol3': 'raven/matrices_cleaned/{}/{}_{}.JPG'.format(
                self.player.matrix_id, self.player.matrix_id, 3),
            'mat_sol4': 'raven/matrices_cleaned/{}/{}_{}.JPG'.format(
                self.player.matrix_id, self.player.matrix_id, 4),
            'mat_sol5': 'raven/matrices_cleaned/{}/{}_{}.JPG'.format(
                self.player.matrix_id, self.player.matrix_id, 5),
            'mat_sol6': 'raven/matrices_cleaned/{}/{}_{}.JPG'.format(
                self.player.matrix_id, self.player.matrix_id, 6),
            'mat_sol7': 'raven/matrices_cleaned/{}/{}_{}.JPG'.format(
                self.player.matrix_id, self.player.matrix_id, 7),
            'mat_sol8': 'raven/matrices_cleaned/{}/{}_{}.JPG'.format(
                self.player.matrix_id, self.player.matrix_id, 8),

            'remaining_time': self.participant.vars['remaining_time'],
            'payment_per_right_raven': c(self.session.config['payment_per_right_raven']),
        }

    # error message for the image selection
    def hidden_answer_error_message(self, hidden_answer):
        answer_key = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '-99': -99,
        }

        self.player.reported_answer = answer_key[str(hidden_answer)]

        correct_answer = self.player.matrix_solution
        if self.round_number == 1:
            self.player.participant.vars['score'] = 0

    #    if correct_answer != self.player.reported_answer:
    #        self.player.num_incorrect_attempts = self.player.num_incorrect_attempts + 1

    #        return "Sorry, that answer was incorrect. Please try again."


    # After each puzzle, we need to calculate the time spent on the page.
    def before_next_page(self):

        if self.round_number == 1:
            self.participant.vars['times'] = []
        #    self.participant.vars['nums_incorrect'] = []
        #    self.participant.vars['total_raven_bonus'] = 0
        #    self.participant.vars['matrices_correctly_answered'] = 0
            self.player.participant.vars['score'] = 0

        if self.player.reported_answer != -99:
            if self.player.reported_answer == self.player.matrix_solution:
                self.player.participant.vars['score'] += 1
            else:
                self.player.participant.vars['score'] -= 1

        self.player.set_score()
        #self.player.participant.vars['score'] += 1
        self.participant.vars['timestamps'].append(time.time()) # time stamps were initiated in the previous page
        self.player.time = self.participant.vars['timestamps'][self.round_number] - \
                           self.participant.vars['timestamps'][self.round_number-1]  # difference between the two most recent timestamps will give the time spent on this page
        self.participant.vars['times'].append(self.player.time)
        #self.participant.vars['nums_incorrect'].append(self.player.num_incorrect_attempts)


        self.participant.vars['remaining_time'] = self.participant.vars['remaining_time'] - int(floor(self.player.time))
        print(self.participant.vars['remaining_time'])

        #increment each time a page is completed (ie a matrix) - rounds that are passed 
        #because time's up won't increment payment
        #Actually also pay for the last one, will make people happy
        #self.participant.vars['matrices_correctly_answered'] = self.participant.vars['matrices_correctly_answered'] + 1
        #self.participant.vars['total_raven_bonus'] = self.participant.vars['total_raven_bonus'] + self.session.vars['bonus_per_matrix']

        self.player.set_payoff()

class Introduction_IQ(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'num_questions':            self.session.vars['num_questions'],
            'time_iq':                  int(round(self.session.config['time_iq']/60)),
            'payment_per_right_raven':        c(self.session.config['payment_per_right_raven']),
        }
    
    
page_sequence = [Introduction_IQ, IQTest]
