from otree.api import *
import random
from iomotions.otree.pages import ScenePage

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
    secret_number = models.IntegerField()
    ans1 = models.StringField()
    ans2 = models.StringField()
    knowledge_check = models.StringField(
        choices=[['True', 'True'], ['False', 'False']],
        label='1. If the computer displays a secret number 4, you can only report or send 4 tokens to player2.',
        widget=widgets.RadioSelect,
    )
    player2_question = models.StringField(
        choices=[['A. The exact value of the secret number', 'A. The exact value of the secret number'],
                 ['B. The number you report', 'B. The number you report'],
                 ['C. The secret number is between 0-10', 'C. The secret number is between 0-10'],
                 ['D. A & B', 'D. A & B'], ['E', 'E. B & C']],
        label='2. Player 2 will receive the following information',
        widget=widgets.RadioSelect,
    )


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
    form_model = 'player'
    form_fields = ['knowledge_check', 'player2_question']
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    '''
    @staticmethod
    def before_next_page(player: Player, timeout_happened):

        player.ans1 = player.knowledge_check
        player.ans2 = player.player2_question
    '''
    @staticmethod
    def error_message(player, values):

        if values['knowledge_check'] == 'True':
            return 'The answer for first question is False. Player 1 can send any number of tokens as they wish.'

        if values['player2_question'] != 'E':
            return 'The answer for second question is option E.'

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
