from .base import *
from decouple import config

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
PREPEND_WWW = True
SESSION_COOKIE_SECURE = True
DEBUG = False

try:
    from .local import *
except ImportError:
    pass
