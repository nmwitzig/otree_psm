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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'altruism_hypothetical'
    players_per_group = None
    num_rounds = 1

    endowment = 1000


class Subsession(BaseSubsession):

    def creating_session(self):
        for p in self.get_players():
            p.participant.vars['part_index'] = 0

            if self.round_number == 1:
                p.participant.vars['part_index'] += 1


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    altruism_hypothetical = models.IntegerField(
        min=0, max=Constants.endowment,
        label=''
    )

