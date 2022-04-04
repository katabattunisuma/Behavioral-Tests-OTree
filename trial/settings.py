from os import environ


SESSION_CONFIGS = [



    dict(
        name='minus', display_name="Stress Test", app_sequence=['Itroduce','minus'], num_demo_participants=3
    ),
    dict(
        name='Wordlist',
        display_name='Word List Learning',
        num_demo_participants=1,
        app_sequence=['Wordlist']
    ),

    dict(
        name='Letter', display_name="Letter identification test", app_sequence=['Letter'], num_demo_participants=1
    ),
    dict(
        name='ravens',
        display_name='Raven\'s Matrix',
        num_demo_participants=3,
        app_sequence=['ravens']
    ),
    dict(
        name='HoltnLaury',
        display_name='Holt and Laury',
        num_demo_participants=1,
        app_sequence=['HoltnLaury']
    ),
    dict(
        name='Hidden_lies',
        display_name='Hidden Lies Task',
        num_demo_participants=1,
        app_sequence=['Hidden_lies']
    ),

    dict(
        name='survey',  display_name='Survey', app_sequence=['survey'], num_demo_participants=1
    ),

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = [
    dict(
        name='Control_Base',
        display_name='Control_Base',
        participant_label_file='_rooms/econ101.txt',
    ),
dict(
        name='Experimental_both',
        display_name='Experimental_both',
        participant_label_file='_rooms/econ101.txt',
    ),
dict(
        name='Experimental_views',
        display_name='Experimental_views',
        participant_label_file='_rooms/econ101.txt',
    ),
dict(
        name='Experimental_scent',
        display_name='Experimental_scent',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('suma')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '8152530668948'

INSTALLED_APPS = ['otree']
