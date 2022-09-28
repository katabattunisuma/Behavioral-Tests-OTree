from otree.api import *
import random
from iomotions.otree.pages import ScenePage
#from iomotions.otree.pages import ScenePage
doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Hidden_lies'
    PLAYERS_PER_GROUP = None
    percent = random.randint(1, 100)
    if percent < 25:
        NUM_ROUNDS = random.randint(20, 27)
    else:
        NUM_ROUNDS = 20

'''class QuizPage(ScenePage):
    scene_name = 'Hidden_lies'
    '''


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    number_entered = models.IntegerField(label="How many tokens do you want to send to player 2",max=10,min=0)
    result1 = models.IntegerField()
    secret_number=models.IntegerField()


# PAGES
class Player1(ScenePage):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Direction(ScenePage):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Quizpage(ScenePage):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Mypage(ScenePage):
    form_model = "player"
    form_fields = ["number_entered"]
    #timeout_seconds = 10

    @staticmethod
    def vars_for_template(player):
        number1 = random.randint(3,8)
        player.secret_number = number1
        return {
            "number1": number1,
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):

        player.payoff = 10-player.number_entered

class Temp(ScenePage):
    pass

class Results(ScenePage):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [Direction,Player1,Quizpage, Mypage, Results]
