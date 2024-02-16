from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent



DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


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