import os
import json
from .confSett import securFileHome, securFileSena

config = securFileHome()

def extensions():
    validExt = ['csv', 'json', 'xlsx', 'pdf', 'html', 'xml', 'sql', 'db', 'py', 'css', 'js']
    validExtPro = ['csv', 'json', 'xlsx', 'xml']
    return validExt, validExtPro


def dbSqlite(BASE_DIR):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'senadlake.db'),
        }
    }

    return DATABASES
    

def dbmariadb(BASE_DIR):
    DATABASES = {
	'default': {
	    'ENGINE': 'django.db.backends.mysql', 
	    'NAME': 'senadlake',
	    'USER': config["MARIADB_USER"],
	    'PASSWORD': config["MARIADB_PASSWORD"],
	    'HOST': 'localhost',
	    'PORT': int(config["MARIADB_PORT"]),
	}
    }
    
    return DATABASES

