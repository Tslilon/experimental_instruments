from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv
import random

author = 'William Murdock (wmurdock@g.harvard.edu) and Pierre-Luc Vautrey (pl.vautrey@gmail.com)'

doc = """
This app goes through 30 raven matrices or as many as can be done in a given time and collects responses and times
"""



class Constants(BaseConstants):
    name_in_url = 'iq_test'
    players_per_group = None

    # number of rounds

    with open('iq_test/Answers.csv') as matrix_file:
        num_rounds = len(list(csv.DictReader(matrix_file)))
    #    num_questions = len(list(csv.DictReader(matrix_file)))

    # load matrix ids and answers.
    # This file should only have the 6 that we voted on including in the incentivized portion


class Subsession(BaseSubsession):
    def creating_session(self):
        with open('iq_test/Answers.csv') as matrix_file:
            self.session.vars['matrices'] = list(csv.DictReader(matrix_file))
        self.session.vars['num_questions'] = len(self.session.vars['matrices'])
        for p in self.get_players():
            p.participant.vars['remaining_time'] = p.session.config['time_iq']
            p.participant.vars['consent'] = 0
            p.participant.vars['passed_screening'] = 0

        for p in self.get_players():
            
            # grab matrix id and matrix solution for the given round.
            # note that we need a slightly different method for practice puzzles and incentivized puzzles
            matrix_data = p.current_matrix()
            p.matrix_id = int(matrix_data['id'])
            p.matrix_solution = int(matrix_data['answer'])

            # initialize the number of incorrect attempts variable (for the given round) to zero
            #p.num_incorrect_attempts = 0

            # randomly sort the solution images for each matrix
            # random_sol_images = random.sample(list(range(1, 9)), 8)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # fields for the main raven pages
    hidden_answer = models.IntegerField()  # which solution pic they clicked on
    #num_incorrect_attempts = models.IntegerField(initial = 0)  # how many incorrect attempts they took
    time = models.FloatField()  # how much time they took on a puzzle
    matrix_id = models.IntegerField()  # puzzle id
    matrix_solution = models.IntegerField()  # solution for the given puzzle
    reported_answer = models.IntegerField()
    # variables to store the randomly sorted solution images
    score = models.IntegerField()

    def set_score(self):
        self.score = self.participant.vars['score']

    def set_payoff(self):
        self.participant.vars['raven_payment'] = c(max(0,self.participant.vars['score']*self.session.config['payment_per_right_raven']))

    participant_vars_dump = models.StringField()

    def current_matrix(self):
        return self.session.vars['matrices'][self.round_number - 1]

    # function to call the current matrix

