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
    final_tokens=models.IntegerField(initial=0)
    answer = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8])
    ans_correct = models.IntegerField(initial=0)


# FUNCTIONS
def creating_session(subsession: Subsession):
    # this is run before the start of every round
    if subsession.round_number == 1:
        for p in subsession.get_players():
            p.participant.vars['payoff_ravens'] = 0


# PAGES
class StartPage(ScenePage):
    @staticmethod
    def is_displayed(player: Player):
        #if player.round_number == 1:
            #print('This is the start of Ravens tests')
        return player.round_number == 1 #and (not player.session.config['debug'])

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
    form_model = 'player'
    form_fields = ['answer']

    @staticmethod
    def get_timeout_seconds(player: Player):
        return player.participant.vars['expiry_timestamp'] - time.time()

    @staticmethod
    def vars_for_template(player: Player):
        return {'image_path': 'ravens/{}.jpg'.format(arr[player.round_number])}
        #return {'image_path': 'ravens/9.jpg'.format(player.round_number)}
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
            if temp.payoff != 0:
                player.final_tokens += temp.ans_correct
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
    Intro,
    Introduction,
    QuestionPage,
    Results,
    Last,
]
