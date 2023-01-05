import random
import time

from otree.api import *

from . import models
from iomotions.otree.pages import ScenePage

'''class QuizPage(ScenePage):
    scene_name = 'Ravens' '''

doc = """
Raven's progressive matrices test measuring cognitive ability
"""
arr=[0,1,2,3,4,9,11,7,8]

class Constants(BaseConstants):
    name_in_url = 'ravens'
    players_per_group = None
    minutes_given = 5
    payment_per_question = 0.5
    num_rounds = 8
    answer_keys = [4, 2, 2, 1, 2, 7, 3, 5, 2, 5, 6, 4]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    final_tokens=models.IntegerField(initial=0)
    answer = models.IntegerField(initial=0, choices=[1, 2, 3, 4, 5, 6, 7, 8])
    ans_correct = models.IntegerField(initial=0)


# FUNCTIONS
def creating_session(subsession: Subsession):
    # this is run before the start of every round
    if subsession.round_number == 1:
        for p in subsession.get_players():
            p.participant.vars['payoff_ravens'] = 0


def get_timeout_seconds(player):
    return player.participant.vars['expiry_timestamp'] - time.time()

# PAGES
class StartPage(ScenePage):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Intro(ScenePage):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Introduction(ScenePage):
    #timeout_seconds = 120

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # user has 5 minutes to complete as many pages as possible
        player.participant.vars['expiry_timestamp'] = time.time() + Constants.minutes_given * 60


class Last(ScenePage):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds


class QuestionPage(ScenePage):
    timer_text = 'Total time left to complete this section:'

    form_model = 'player'
    form_fields = ['answer']
    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def get_timeout_seconds(player: Player):
        return player.participant.vars['expiry_timestamp'] - time.time()

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

    @staticmethod
    def vars_for_template(player: Player):
        return {'image_path': 'ravens/{}.jpg'.format(arr[player.round_number])}

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.answer = 0
        if player.answer == Constants.answer_keys[arr[player.round_number]-1]:
            if player.round_number == 4 or player.round_number == 7:
                player.ans_correct = 1
            elif player.round_number == 1 or player.round_number == 2 or player.round_number == 5:
                player.ans_correct = 2
            else:
                player.ans_correct = 4


class Results(ScenePage):
    #timeout_seconds = 60

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds

    @staticmethod
    def vars_for_template(player: Player):
        all_players = player.in_all_rounds()
        player.final_tokens = 0
        for temp in all_players:
            if temp.ans_correct != 0:
                player.final_tokens += temp.ans_correct

        if player.in_round(8).answer != 0:
            player.final_tokens += 1

        player.payoff = player.final_tokens * Constants.payment_per_question

        return {
            'total_correct': player.final_tokens,
            'earnings': player.payoff,
        }


page_sequence = [
    Intro,
    Introduction,
    QuestionPage,
    Results,
    Last,
]
