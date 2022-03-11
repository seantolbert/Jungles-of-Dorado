from decouple import config

DEPLOY_MODE=config('DEPLOY_MODE')

if DEPLOY_MODE == 'dev':
    from .dev import *
elif DEPLOY_MODE == 'production':
    from .production import *
