from .base import *
from decouple import config

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
PREPEND_WWW = True
SESSION_COOKIE_SECURE = True
DEBUG = False
SECRET_KEY = config('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = ['www.junglesofdorado.com']
MEDIA_URL = "https://%s/" % '%s.s3.amazonaws.com' % config('AWS_STORAGE_BUCKET_NAME')
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


try:
    from .local import *
except ImportError:
    pass
