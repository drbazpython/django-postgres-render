"""
     Customised Logging

     To use in a class or function:
     - import logging
     - import environ
    if LOG_LEVEL is in a .env file:
        - env = environ.Env()
        - environ.Env.read_env()

     - log = logging.getLogger(__name__)
     - log.debug("message")

     - for logger_name in ('myproject')
"""

import environ

env = environ.Env()
environ.Env.read_env()

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters':{
        'standard': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s', 
            'datefmt':'%d-%m-%Y',
        },
    },
    'handlers': {
        'console': {
            'level': env('LOG_LEVEL'),
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'filters': [],
        },
    },
    'loggers': {
        logger_name: {
            'level': env('LOG_LEVEL'),
            'propagate': True,
        } for logger_name in ('myproject', 'myapp')
    },
    'root': {
        'level': env('LOG_LEVEL'),
        'handlers': ['console'],
    },
}

