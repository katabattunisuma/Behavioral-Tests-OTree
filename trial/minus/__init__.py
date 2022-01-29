from otree.api import *
import random

from otree.models import player

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'minus'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 30
    Payment_for_one_correct = 1



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    number_entered = models.IntegerField(label="Enter your answer")
    result1 = models.IntegerField()
    final_tokens=models.IntegerField(initial=0)


# PAGES
class Direction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
class MyPage(Page):
    form_model = "player"
    form_fields = ["number_entered"]
    timeout_seconds = 10
    @staticmethod
    def vars_for_template(player):
        number1 = random.randint(1000, 9999)
        number2 = random.randint(10, 99)
        player.result1 = number1-number2

        return{
            "number1": number1,
            "number2": number2,

        }
    @staticmethod
    def before_next_page(player: Player, timeout_happened):

        if player.number_entered == player.result1:
            player.payoff = C.Payment_for_one_correct
        else:
            player.payoff = 0


class Results(Page):
    pass

class Final_Results(Page):
    form_model = "player"
    #form_fields = ["final_tokens"]
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    @staticmethod
    def vars_for_template(player: Player):
        all_players = player.in_all_rounds()
        player.final_tokens=0
        for temp in all_players:
            if temp.payoff == 1:
                player.final_tokens+=1
            else:
                player.final_tokens=0



page_sequence = [Direction,MyPage, Results,Final_Results]
