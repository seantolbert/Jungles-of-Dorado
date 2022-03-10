from .base import *

DEBUG = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
PREPEND_WWW = True
SESSION_COOKIE_SECURE = True

try:
    from .local import *
except ImportError:
    pass
