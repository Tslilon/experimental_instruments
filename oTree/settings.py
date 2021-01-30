from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 10.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
      'name': 'test_session',
      'display_name': 'Test Session',
      'num_demo_participants': 1,
      'app_sequence': ['test_session', ],
    }, 

]



# [

#     {
#     	'name': 'bret',
#     	'display_name': 'Bomb Risk Elicitation Task',
#     	'num_demo_participants': 1,
#     	'app_sequence': ['bret', ],
#     }, 
#     {
#         'name': 'pre_slider',
#         'display_name': "Pre-Task Self-Rating",
#         'num_demo_participants': 1,
#         'app_sequence': ['pre_slider', ],
#     },
#     {
#         'name': 'radioselect_pre',
#         'display_name': "Pre-Task Self-Rating V2",
#         'num_demo_participants': 1,
#         'app_sequence': ['radioselect_pre', ],
#     },
#     {
#         'name': 'iq_test',
#         'display_name': "Raven's Test",
#         'num_demo_participants': 1,
#         'app_sequence': ['iq_test', ],
#     },
#     {
#         'name': 'ravens',
#         'display_name': "Raven's Test",
#         'num_demo_participants': 1,
#         'app_sequence': ['ravens', ],
#     },
#     {
#         'name': 'post_slider',
#         'display_name': "Post-Task Self-Rating",
#         'num_demo_participants': 1,
#         'app_sequence': ['post_slider', ],
#     },
#     {
#         'name': 'pre_prob',
#         'display_name': "Pre-Info Probability",
#         'num_demo_participants': 1,
#         'app_sequence': ['pre_prob', ],
#     },
#     {
#         'name': 'post_prob',
#         'display_name': "Post-Info Probability",
#         'num_demo_participants': 1,
#         'app_sequence': ['post_prob', ],
#     },
# ]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

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
INSTALLED_APPS = ['test_session']
