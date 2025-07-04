from os import environ
from dotenv import load_dotenv
load_dotenv('../secrets.env')

SESSION_CONFIGS = [
    dict(
        name='mftrust',
        display_name="A Framed Trust Game with Message Option",
        app_sequence=['mftrust'],
        num_demo_participants=2,
    ),
    dict(
        name='grief_support',
        display_name="Grief Support Interaction Game",
        app_sequence=['grief_support'],
        num_demo_participants=2,
    ),
    dict(
        name='stakeholder',
        display_name="A Stakeholder Game",
        app_sequence=['stakeholder'],
        num_demo_participants=1,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['wealth', 'part_id', 'well_being']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

SECRET_KEY = environ.get('OTREE_REST_KEY')

INSTALLED_APPS = ['otree']
