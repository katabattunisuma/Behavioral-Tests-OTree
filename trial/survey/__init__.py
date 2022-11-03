from otree.api import *

from iomotions.otree.pages import ScenePage
class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female'],['Others','Others'],['Don\'t want to say','Don\'t want to say']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    age = models.IntegerField(label='What is your age?', min=13, max=125)
    identification = models.StringField(
        choices=[['Non-Hispanic White', 'Non-Hispanic White'], ['Non-Hispanic Black', 'Non-Hispanic Black'],
                 ['Non-Hispanic Asian', 'Non-Hispanic Asian'],
                 ['Mexican American', 'Mexican American'],['Other Hispanic', 'Other Hispanic'], ['Others', 'Others'],
                 ['Don\'t want to say', 'Don\'t want to say']],
        label='What would you best identify as?',
        widget=widgets.RadioSelect,
    )

    other_category = models.StringField(label='If you selected Others for the above question, please specify.')
    education = models.StringField(
        choices=[['Bachelors', 'Bachelors'], ['Masters', 'Masters'],
                 ['PhD/Doctorate', 'PhD/Doctorate'],
                 ['Others', 'Others']],
        label='What is your current educational classification?',
        widget=widgets.RadioSelect,
    )
    level = models.StringField(
        choices=[['Freshman', 'Freshman'], ['Sophomore', 'Sophomore'],
                 ['Junior', 'Junior'],
                 ['Senior', 'Senior'], ['Grad/Professional','Grad/Professional']],
        label='Which is your class?',
        widget=widgets.RadioSelect,
    )
    major = models.StringField(label='What is your major? (Mention if any dual majors or minors):')
    hours_classes = models.StringField(
        choices=[['0-1 hour', '0-1 hour'], ['1-3 hours', '1-3 hours'],
                 ['3-5 hours', '3-5 hours'],
                 ['5 hours or more', '5 hours or more']],
        label='How many hours of classes did you have today?',
        widget=widgets.RadioSelect,
    )
    hours_work = models.StringField(
        choices=[['0-1 hour', '0-1 hour'], ['1-3 hours', '1-3 hours'],
                 ['3-5 hours', '3-5 hours'],
                 ['5 hours or more', '5 hours or more']],
        label='How many hours did you work today?',
        widget=widgets.RadioSelect,
    )

    '''work_schedule = models.StringField(
        choices=[['Mornings(8-Noon)', 'Mornings(8-Noon)'], ['Afternoons(Noon-5PM)', 'Afternoons(Noon-5PM)'],
                 ['Evenings(5PM-10PM)', 'Evenings(5PM-10PM)'],
                 ['Nights(Later than 10PM)', 'Nights(Later than 10PM)']],
        label='What times are your work scheduled at? (Select all that apply)',
        widget=widgets.RadioSelect,
    )'''
    work_schedule = models.StringField(label='What times are your work scheduled at? <br> 1. Mornings(8-Noon) <br>'
                                             '2.Afternoons(Noon-5PM) <br>'
                                             '3. Evenings(5PM-10PM) <br>'
                                             '4. Nights(Later than 10PM) <br>'
                                             'Enter all that apply as comma separated values Eg: 1,3')
    tired = models.StringField(
        choices=[['8-9PM', '8-9PM'], ['9-10:15PM', '9-10:15PM'],
                 ['10:15-12:30PM', '10:15-12:30PM'],
                 ['12:30-1:45AM', '12:30-1:45AM'],['1:45-3AM', '1:45-3AM'],['3AM or later', '3AM or later']],
        label='At what time in the evenings,do you feel tired and as a result, in need of sleep?',
        widget=widgets.RadioSelect,
    )
    hours_sleep = models.StringField(
        choices=[['0-2 hour', '0-2 hour'], ['5-8 hours', '5-8 hours'],
                 ['8-10 hours', '8-10 hours'],
                 ['10 hours or more', '10 hours or more']],
        label='How many hours of sleep did you get last night?',
        widget=widgets.RadioSelect,
    )
    best_time = models.StringField(
        choices=[['8-10AM', '8-10AM'], ['11AM-1PM', '11AM-1PM'],
                 ['3-5PM', '3-5PM'],
                 ['7-9PM', '7-9PM']],
        label='You wish to be at your peak performance for a test which you know is ging to be mentally exhausting and last for 2 hours: you are entirely free to plan your day and considering only your own \"feelong best\" rhythm, which one of the four following times would you choose?',
        widget=widgets.RadioSelect,
    )
    tired_level = models.StringField(
        choices=[['Not at all', 'Not at all'], ['A little tired', 'A little tired'],
                 ['Fairly tired', 'Fairly tired'],
                 ['Very tired', 'Very tired']],
        label='If you went to bed at 11PM, what level of tiredness would you be?',
        widget=widgets.RadioSelect,
    )
    feel_best = models.StringField(
        choices=[['12-4AM', '12-4AM'], ['4-7AM', '4-7AM'],
                 ['7-9AM', '7-9AM'],
                 ['9AM-4PM', '9AM-4PM'],['4-10PM', '4-10PM'],['10PM-121M', '10PM-12AM']],
        label='At what time of the day do you feel you are at your \"feeling best\" peak?',
        widget=widgets.RadioSelect,
    )
    personality = models.StringField(
        choices=[['Definitely a \"morning\" type', 'Definitely a \"morning\" type'], ['Rather a \"morning\" type than \"evening\"', 'Rather a \"morning\" type than \"evening\"'],
                 ['Rather an \"evening\" type than \"morning\"', 'Rather an \"evening\" type than \"morning\"'],
                 ['Definitely a \"evening\" type', 'Definitely a \"evening\" type']],
        label='One hears about "Morning" and "Evening" types of people. Which one of these types would you consider yourself to be?',
        widget=widgets.RadioSelect,
    )
    stress_level = models.StringField(
        choices=[['Not at all stressed', 'Not at all stressed'], ['A little stressed', 'A little stressed'],
                 ['Fairly stressed', 'Fairly stressed'],
                 ['A lot stressed', 'A lot stressed']],
        label='How stressed would you say you were before this study?',
        widget=widgets.RadioSelect,
    )
    mental_math = models.StringField(
        choices=[['No changes in stress levels', 'No changes in stress levels'], ['A little less stressed', 'A little less stressed'],
                 ['A lot less stressed', 'A lot less stressed stressed'],['A little more stressed', 'A little more stressed'],
                 ['A lot more stressed', 'A lot more stressed']],
        label='How stressed would you say you were after the first phase of study: The Mental Math task?',
        widget=widgets.RadioSelect,
    )
    mini_break = models.StringField(
        choices=[['Not at all', 'Not at all'], ['A little', 'A little'],
                 ['Fair amount', 'Fair amount'],
                 ['A lot', 'A lot']],
        label='How did the mini breaks affect your stress levels?',
        widget=widgets.RadioSelect,
    )
    outdoor_time = models.StringField(
        choices=[['Not at all','Not at all'],['Some but less than 30 minutes','Some but less than 30 minutes'],['30 mins- 1hour','30 mins- 1hour'],['1-2 hours','1-2 hours'], ['2-3 hours', '2-3 hours'],
                 ['3-4 hours', '3-4 hours'],['4-5 hours', '4-5 hours'],
                 ['5-7 hours', '5-7 hours'],
                 ['7 hours or more', '7 hours or more']],
        label='In the last week, when the weather allows, about how long on an average do you spend outdoors in nature?',
        widget=widgets.RadioSelect,
    )
    objective=models.LongStringField(label='What do you think the objective of this study was?')
    surroundings = models.StringField(
        choices=[['Yes', 'Yes'], ['No', 'No']],
        label='Did you notice your visual surroundings, windows, views, or such?',
        widget=widgets.RadioSelect,
    )
    indoor_conditions = models.StringField(
        choices=[['Yes', 'Yes'], ['No', 'No']],
        label='Did you notice indoor conditions - Temperature, Scents, lighting, etc.,',
        widget=widgets.RadioSelect,

    )
    screen_time = models.StringField(
        choices=[['0-1 hours', '0-1 hours'],['1-2 hours', '1-2 hours'], ['2-4 hours', '2-4 hours'],
                 ['4-6 hours', '4-6 hours'],['6 hours or more', '6 hours or more']],
        label='How many hours do you typically spend on screen (Computer, TV, Tablets, Videogames, etc.,) on a daily basis, excluding any work or class hours?',
        widget=widgets.RadioSelect,
    )
    proficiency = models.StringField(
        choices=[['Excellent', 'Excellent'], ['Very Good', 'Very Good'],
                 ['Fair', 'Fair'],
                 ['Little/Not a lot', 'Little/Not a lot'],['Inexperienced','Inexperienced']],
        label='How proficient would you say you are with computers/performing computer tasks?',
        widget=widgets.RadioSelect,
    )
    crt_bat = models.IntegerField(
        label='''
        A bat and a ball cost 22 dollars in total.
        The bat costs 20 dollars more than the ball.
        How many dollars does the ball cost?'''
    )
    crt_widget = models.IntegerField(
        label='''
        If it takes 5 machines 5 minutes to make 5 widgets,
        how many minutes would it take 100 machines to make 100 widgets?
        '''
    )
    crt_lake = models.IntegerField(
        label='''
        In a lake, there is a patch of lily pads.
        Every day, the patch doubles in size.
        If it takes 48 days for the patch to cover the entire lake,
        how many days would it take for the patch to cover half of the lake?
        '''
    )


# FUNCTIONS
# PAGES
class Form1(Page):
    form_model = 'player'
    form_fields = ['gender', 'age','identification','other_category','education','level','major','hours_classes','hours_work','work_schedule']
    #form_fields2=['identification']
class Form2(Page):
    form_model = 'player'
    form_fields = ['tired','hours_sleep','best_time','tired_level','feel_best','personality']
class Form3(Page):
    form_model = 'player'
    form_fields = ['stress_level','mental_math','mini_break','outdoor_time','objective','surroundings','indoor_conditions','screen_time','proficiency']

class CognitiveReflectionTest(Page):
    form_model = 'player'
    form_fields = ['crt_bat', 'crt_widget', 'crt_lake']

class Thankyou(Page):
    form_model = 'player'


page_sequence = [Form1,Form2, Form3, Thankyou]
