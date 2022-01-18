from otree.api import *
import random
import string

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Letter'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 5
    Payment_for_one_correct=1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    number_entered = models.IntegerField(label="Enter your answer")
    result1 = models.IntegerField()
    final_tokens = models.IntegerField(initial=0)
    #my_page_timeout_seconds = models.IntegerField(initial=120)



# PAGES
class Direction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
class MyPage(Page):
    form_model = "player"
    form_fields = ["number_entered"]
    timeout_seconds = 120

    @staticmethod
    def vars_for_template(player: Player):
        text = ''
        for i in range(250):
            if i%50==0:
                text += '\n\n'
            text += random.choice(string.ascii_letters).lower()
        ch=random.choice(string.ascii_letters).lower()
        player.result1 = text.count(ch)
        return {
            "text": text,
            "ch":ch
        }


    @staticmethod
    def before_next_page(player: Player,timeout_happened):

        if player.number_entered == player.result1:
            player.payoff += C.Payment_for_one_correct
        else:
            player.payoff = 0

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
            '''else:
                player.final_tokens=0'''


class Results(Page):
    pass


page_sequence = [Direction,MyPage,Final_Results]
