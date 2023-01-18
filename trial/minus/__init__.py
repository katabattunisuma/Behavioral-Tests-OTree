from otree.api import *
import random
from iomotions.otree.pages import ScenePage
#start_scene_recording(ip_address, scene_name, scene_description = '')

from otree.models import player

doc = """
Your app description
"""
#from iomotions.otree.pages import ScenePage

'''class QuizPage(ScenePage):
    scene_name = 'Stress Test' '''

class C(BaseConstants):
    NAME_IN_URL = 'minus'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 20
    Payment_for_one_correct = 1



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    number_entered = models.IntegerField(label="Enter your answer")
    result1 = models.IntegerField()
    final_tokens = models.IntegerField()
    note = models.StringField()
    temp_earnings = models.IntegerField()


# PAGES
class Direction(ScenePage):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
class MyPage(ScenePage):
    form_model = "player"
    form_fields = ["number_entered"]
    timeout_seconds = 8
    @staticmethod
    def vars_for_template(player):
        number1 = random.randint(1000, 9999)
        number2 = random.randint(10, 99)
        if number2 % 2 == 0:
            number2 += 1
        player.result1 = number1-number2

        return{
            "number1": number1,
            "number2": number2,

        }
    @staticmethod
    def before_next_page(player: Player, timeout_happened):

        if player.number_entered == player.result1:
            player.temp_earnings = 1
        else:
            player.temp_earnings = 0


class Results(ScenePage):
    form_model = "player"
    timeout_seconds = 2

    @staticmethod
    def vars_for_template(player):
        if player.temp_earnings == 0:
            player.note = "Oops!! <br> <h3>Your answer is wrong.</h3>"
        else:
            player.note = "You got it right!! Keep Going."

class Example(ScenePage):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Final_Results(ScenePage):
    form_model = "player"
    #form_fields = ["final_tokens"]
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    @staticmethod
    def vars_for_template(player: Player):
        all_rounds = player.in_all_rounds()
        player.final_tokens=0
        for temp in all_rounds:
            if temp.temp_earnings == 1:
                player.final_tokens += 1
            else:
                player.final_tokens=0
        player.payoff = player.final_tokens

#end_scene_recording(ip_address, scene_name)
page_sequence = [Direction,Example,MyPage,Results,Final_Results]

