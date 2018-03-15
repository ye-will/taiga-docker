from .common import *
import os

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': os.getenv('DB_NAME', 'taiga'),
       'USER': os.getenv('DB_USER', 'taiga'),
       'PASSWORD': os.getenv('DB_PASSWORD', 'password'),
       'HOST': os.getenv('DB_HOST', ''),
       'PORT': os.getenv('DB_PORT', ''),
   }
}

SCHEME = os.getenv("SCHEME", "http")
DOMAIN = os.getenv("DOMAIN", "localhost")

SITES = {
   "api": {
      "scheme": SCHEME,
      "domain": DOMAIN,
      "name": "api"
   },
   "front": {
      "scheme": SCHEME,
      "domain": DOMAIN,
      "name": "front"
   }
}

MEDIA_ROOT = '/taiga/media'
MEDIA_URL = ''.join([SCHEME, '://', DOMAIN, '/media/'])
STATIC_ROOT = '/taiga/static'
STATIC_URL = ''.join([SCHEME, '://', DOMAIN, '/static/'])

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS') == 'True'
EMAIL_HOST = os.getenv('EMAIL_HOST', 'localhost')
EMAIL_PORT = os.getenv('EMAIL_PORT', 25)
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'user')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'password')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'dev@example.com')

DEBUG = os.getenv('DEBUG') == 'True'
TEMPLATE_DEBUG = os.getenv('TEMPLATE_DEBUG') == 'True'
PUBLIC_REGISTER_ENABLED = os.getenv('PUBLIC_REGISTER_ENABLED') != 'False'

if os.environ.get("GITHUB_API_CLIENT_ID"):
    INSTALLED_APPS += ["taiga_contrib_github_auth"]
    GITHUB_API_CLIENT_ID = os.environ.get("GITHUB_API_CLIENT_ID")
    GITHUB_API_CLIENT_SECRET = os.environ.get("GITHUB_API_CLIENT_SECRET")
