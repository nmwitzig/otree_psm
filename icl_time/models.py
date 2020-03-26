from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from icl_time.config import *
import random


author = 'Felix Holzmeister'

doc = """
Staircase risk elicitation task as proposed by Falk et al. (2016), Working Paper.
"""


# ******************************************************************************************************************** #
# *** CLASS SUBSESSION
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):

    # initiate list of sure payoffs and implied switching row in first round
    # ------------------------------------------------------------------------------------------------------------
    def creating_session(self):
        # creating index denoting new App (e.g., Part 'index')
        for p in self.get_players():
            p.participant.vars['part_index'] = 0
            if self.round_number == 1:
                p.participant.vars['part_index'] += 1

        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['icl_time_sure_payoffs'] = [Constants.sure_payoff]
                p.participant.vars['icl_switching_row'] = 2 ** Constants.num_choices


# ******************************************************************************************************************** #
# *** CLASS GROUP
# ******************************************************************************************************************** #
class Group(BaseGroup):
    pass


# ******************************************************************************************************************** #
# *** CLASS PLAYER
# ******************************************************************************************************************** #
class Player(BasePlayer):

    # add model fields to class player
    # ----------------------------------------------------------------------------------------------------------------
    sure_payoff = models.FloatField()
    choice = models.StringField()
    switching_row = models.IntegerField()

    #payoff_ecu = models.FloatField()

    # set sure payoff for next choice
    # ----------------------------------------------------------------------------------------------------------------
    def set_sure_payoffs(self):

        # add current round's sure payoff to model field
        # ------------------------------------------------------------------------------------------------------------
        self.sure_payoff = self.participant.vars['icl_time_sure_payoffs'][self.round_number - 1]

        # determine sure payoff for next choice and append list of sure payoffs
        # ------------------------------------------------------------------------------------------------------------
        if not self.round_number == Constants.num_choices:

            if self.choice == 'A':
                self.participant.vars['icl_time_sure_payoffs'].append(
                    self.participant.vars['icl_time_sure_payoffs'][self.round_number - 1]
                    + Constants.delta / 2 ** (self.round_number - 1)
                )
            elif self.choice == 'B':
                self.participant.vars['icl_time_sure_payoffs'].append(
                    self.participant.vars['icl_time_sure_payoffs'][self.round_number - 1]
                    - Constants.delta / 2 ** (self.round_number - 1)
                )
            else:
                pass

    # update implied switching row each round
    # ----------------------------------------------------------------------------------------------------------------
    def update_switching_row(self):

        if self.choice == 'B':
            self.participant.vars['icl_switching_row'] -= 2 ** (Constants.num_choices - self.round_number)

        elif self.choice == 'I':
            self.participant.vars['icl_switching_row'] /= 2
