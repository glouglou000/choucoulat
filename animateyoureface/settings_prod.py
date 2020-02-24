"""Settings for the prodiction (heroku)"""

#Import settings.
from Synergo.settings import *




ALLOWED_HOSTS = ["animateyoureface.herokuapp.com"]

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
