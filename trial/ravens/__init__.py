import random
import time

from otree.api import *

from . import models


author = 'Huanren Zhang'
doc = """
Raven's progressive matrices test measuring cognitive ability
"""


class Constants(BaseConstants):
    name_in_url = 'ravens'
    players_per_group = None
    minutes_given = 5
    payment_per_question = 1
    payment_in_points = 2
    num_rounds = 8
    answer_keys = [4, 2, 2, 1, 2, 7, 3, 5, 2, 5, 6, 4]
    instructions_template = 'ravens/Instructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8])
    ans_correct = models.BooleanField()


# FUNCTIONS
def creating_session(subsession: Subsession):
    # this is run before the start of every round
    if subsession.round_number == 1:
        for p in subsession.get_players():
            p.participant.vars['payoff_ravens'] = 0


# PAGES
class StartPage(Page):
    @staticmethod
    def is_displayed(player: Player):
        #if player.round_number == 1:
            #print('This is the start of Ravens tests')
        return player.round_number == 1 #and (not player.session.config['debug'])

class Intro(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Introduction(Page):
    #timeout_seconds = 120

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # user has 5 minutes to complete as many pages as possible
        player.participant.vars['expiry_timestamp'] = time.time() + Constants.minutes_given * 60


class Last(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds



class QuestionPage(Page):
    form_model = 'player'
    form_fields = ['answer']

    @staticmethod
    def get_timeout_seconds(player: Player):
        return player.participant.vars['expiry_timestamp'] - time.time()

    @staticmethod
    def vars_for_template(player: Player):
        return {'image_path': 'ravens/{}.jpg'.format(player.round_number)}

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.answer = 0
        player.ans_correct = player.answer == Constants.answer_keys[player.round_number - 1]
        player.participant.vars['payoff_ravens'] += (
            player.ans_correct * Constants.payment_per_question
        )
        if Constants.payment_in_points > 0:
            player.payoff = player.ans_correct * Constants.payment_in_points
        else:
            player.payoff = (
                player.ans_correct
                * Constants.payment_per_question
                / player.session.config['real_world_currency_per_point']
            )  # to measure in point


class Results(Page):
    #timeout_seconds = 60

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'total_correct': sum([p.ans_correct for p in player.in_all_rounds()]),
            'earnings': sum([p.ans_correct for p in player.in_all_rounds()])
            * Constants.payment_per_question,
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        for p in player.subsession.get_players():
            p.participant.vars['payoff_ravens'] = (
                sum([p.ans_correct for p in player.in_all_rounds()])
                * Constants.payment_per_question
            )


page_sequence = [
    #StartPage,
    Intro,
    Introduction,
    QuestionPage,
    Results,
    Last,
]
