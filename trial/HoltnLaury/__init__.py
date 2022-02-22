from otree.api import *
import random

doc = """
Your app description
"""
#from iomotions.otree.pages import ScenePage

'''class QuizPage(ScenePage):
    scene_name = 'HotnLaury' '''

class C(BaseConstants):
    NAME_IN_URL = 'HoltnLaury'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision_made = models.StringField(choices=["A","B"],label="")


# PAGES
class MyPage(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Question(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Decision(Page):
    form_model = "player"
    form_fields = ["decision_made"]
    timeout_seconds = 30

    @staticmethod
    def vars_for_template(player):
        number1 = round(random.uniform(1.8, 2.2),2)
        number2 = round(random.uniform(1.4, 1.8),2)
        number3 = round(random.uniform(3.4, 3.85),2)
        number4 = round(random.uniform(0.10, 0.60),2)

        return {
            "number1": number1,
            "number2": number2,
            "number3": number3,
            "number4": number4,

        }

class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [MyPage, Question, Decision, Results]
