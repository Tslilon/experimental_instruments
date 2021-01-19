from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1

class Time_Preference(Page):
    form_model = 'player'
    form_fields = ['decision']

    def vars_for_template(self):

        # specify info for progress bar
        total = Constants.num_rounds
        page = self.subsession.round_number
        progress = page / total * 100

        return {
            'page':        page,
            'total':       total,
            'progress':    progress,
        }

    def before_next_page(self):
        self.player.set_payoff()

        if self.round_number == Constants.num_rounds:
            print(self.round_number)
            payoff_now_arr = []
            payoff_later_arr = []
            now_or_later = []
            x = random.randint(0,Constants.num_rounds-1)
            for i in range(1,Constants.num_rounds+1):
                payoff_now_arr.append(self.player.in_round(i).payoff_now)

                payoff_later_arr.append(self.player.in_round(i).payoff_later)
                now_or_later.append(self.player.in_round(i).decision)

            if now_or_later[x]:
                self.participant.vars['time_payment'] = c(payoff_later_arr[x])
                self.participant.vars['payoff_timing'] = Constants.future_date
            else:
                self.participant.vars['time_payment'] = c(payoff_now_arr[x])
                self.participant.vars['payoff_timing'] = "today"
            # if now_or_later[x]:
            #     y = payoff_later_arr[x]
            #     z = payoff_now_arr[x]
            # else:
            #     y = payoff_now_arr[x]
            #     z = payoff_later_arr[x]
            #
            # if y[x] == 0:
            #     self.participant.vars['time_payment'] = c(z)
            #     self.participant.vars['payoff_timing'] = "today"
            # else:
            #     self.participant.vars['time_payment'] = c(y)
            #     self.participant.vars['payoff_timing'] = Constants.future_date

            self.player.payoff = self.participant.vars['time_payment']

            self.participant.vars['p_TimePref_now'] = payoff_now_arr
            self.participant.vars['p_TimePref_later'] = payoff_later_arr
            self.participant.vars['TimePref_now_or_later'] = now_or_later


page_sequence = [
    Instructions,
    Time_Preference
]
