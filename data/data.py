from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent



# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }


# DATABASES = {
#     "default":{
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'railway',
#         'USER': 'postgres',
#         'PASSWORD': '-EA6edd*1F6F-d26aGDBBB45A232edcG',
#         'HOST': 'viaduct.proxy.rlwy.net',
#         'PORT': '33627',
#     }
# }


DATABASES = {
    "default":{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT'),
    }
}