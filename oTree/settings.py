from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

LANGUAGE_CODE = 'en' #Switch between English and Hebrew
RANDOMIZATION = True #True for random session, False for admin control (manually assign treatment)


SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 10.00,
    'participation_fee': 0.00,
    'doc': "",
}

# if RANDOMIZATION == True:
#     SESSION_CONFIGS = [
#     {
#       'name': 'test_session_randomized',
#       'display_name': 'Test Session Randomized',
#       'app_sequence': ['ravens', 'confidence_info_treatment'],
#       'num_demo_participants': 1,
#     }]
# else:
#     SESSION_CONFIGS = [
#     {
#       'name': 'test_session_with_info',
#       'display_name': 'Test Session with Info',
#       'app_sequence': ['ravens', 'confidence_info_treatment'],
#       'num_demo_participants': 1,
#       'treatment': 'with_info'
#     }, 
#     {
#       'name': 'test_session_without_info',
#       'display_name': 'Test Session without Info',
#       'app_sequence': ['ravens', ],
#       'num_demo_participants': 1,
#       'treatment': 'without_info'
#     }]

SESSION_CONFIGS = [{
  'name': 'questionnaire',
  'display_name': 'Questionnaire',
  'app_sequence': ['unincentivized_Q'],
  'num_demo_participants': 1,
}]

# SESSION_CONFIGS = [
#     {
#     	'name': 'bret',
#     	'display_name': 'Bomb Risk Elicitation Task',
#     	'num_demo_participants': 1,
#     	'app_sequence': ['bret', ],
#     }]


# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'r=-3zk)@=f38^)%j#&$4m3c*)7y55ly6s*ww-fwjtzjhb54ude'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
# INSTALLED_APPS = ['bret']
# INSTALLED_APPS = ['ravens', 'confidence_info_treatment']
INSTALLED_APPS = ['unincentivized_Q']
