from .base import *

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
PREPEND_WWW = True
SESSION_COOKIE_SECURE = True
DEBUG = False
SECRET_KEY = config('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = ['www.junglesofdorado.com']

try:
    from .local import *
except ImportError:
    pass
