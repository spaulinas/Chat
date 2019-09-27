# czat1/settings.py

INSTALLED_APPS = [
    'czat.apps.CzatConfig', # rejestrujemy aplikacje czat
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LANGUAGE_CODE = 'pl'  # ustawienie jezyka

TIME_ZONE = 'Europe/Warsaw'  # ustawienie strefy czasowej
