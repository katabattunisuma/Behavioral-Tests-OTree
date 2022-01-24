from otree.api import Currency as cu, currency_range
from . import *
from otree.api import Bot



class PlayerBot(Bot):

    def play_round(self):
        # yield (StartPage)
        if self.subsession.round_number == 1:
            yield (Introduction)
        yield (QuestionPage, {'answer': Constants.answer_keys[self.subsession.round_number-1]})
        if self.subsession.round_number == Constants.num_rounds:
            yield (Results)
