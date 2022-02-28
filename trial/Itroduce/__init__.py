from otree.api import *


doc = """
Your app description
"""
#from iomotions.otree.pages import ScenePage

'''class QuizPage(ScenePage):
    scene_name = 'Introduction' '''

class C(BaseConstants):
    NAME_IN_URL = 'Itroduce'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Page1(Page):
    pass

class Page2(Page):
    pass

class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage]
