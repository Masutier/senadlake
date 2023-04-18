import os

def dbSqlite(BASE_DIR):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'senadlake.db'),
        }
    }

    return DATABASES
