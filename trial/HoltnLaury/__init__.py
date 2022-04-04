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
    PAYMENT_FOR_EACH_CORRECT_ANSWER = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision_made = models.StringField(choices=["A","B"],label="")
    num1 = models.FloatField()
    num2 = models.FloatField()
    num3 = models.FloatField()
    num4 = models.FloatField()
    payoff_if_dice_is_1 = models.CurrencyField()
    payoff_if_dice_is_2to10 = models.CurrencyField()
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
        player.num1 = number1
        player.num2 = number2
        player.num3 = number3
        player.num4 = number4

        return {
            "number1": number1,
            "number2": number2,
            "number3": number3,
            "number4": number4,
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.decision_made == 'A':
            player.payoff_if_dice_is_1 = player.num1*C.PAYMENT_FOR_EACH_CORRECT_ANSWER
            player.payoff_if_dice_is_2to10 = player.num2 * C.PAYMENT_FOR_EACH_CORRECT_ANSWER
        elif player.decision_made == 'B':
            player.payoff_if_dice_is_1 = player.num3 * C.PAYMENT_FOR_EACH_CORRECT_ANSWER
            player.payoff_if_dice_is_2to10 = player.num4 * C.PAYMENT_FOR_EACH_CORRECT_ANSWER
        else :
            player.payoff_if_dice_is_1 = 0
            player.payoff_if_dice_is_2to10 = 0





class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [MyPage, Question, Decision, Results]
