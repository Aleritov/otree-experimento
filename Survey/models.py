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


author = 'Jason Friedman, Student Helper COG, ETHZ'

doc = """
Link to a survey.
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = 10
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
