from pathlib import Path
from environs import Env


env = Env()
env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = env('DJANGO_SECRET_KEY', default='django-insecure-replace-this-key')
DEBUG = env.bool('DEBUG', default=True)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

# -----------------------------
# Aplicaciones
# -----------------------------
INSTALLED_APPS = [
    'authentication',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'banking.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'banking.wsgi.application'

# -----------------------------
# Base de datos
# -----------------------------
DATABASES = {
    'postgres_local': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': env('DB_HOST', default='localhost'),
        'NAME': env('DB_NAME', default='banking'),
        'USER': env('DB_USER', default='postgres'),
        'PASSWORD': env('DB_PASSWORD', default='unicesmag'),
        'PORT': env('DB_PORT', default='5432'),
    },
    'supabase': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': env('SUPA_DB_HOST', default='aws-1-us-east-2.pooler.supabase.com'),
        'NAME': env('SUPA_DB_NAME', default='postgres'),
        'USER': env('SUPA_DB_USER', default='postgres.hfkljxcwfdzddpazvdsr'),
        'PASSWORD': env('SUPA_DB_PASSWORD', default='unicesmag'),
        'PORT': env('SUPA_DB_PORT', default='6543'),
    },
    'local_sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'banking.sqlite3',
    }
}

# Elegir base de datos activa
ENV = env('ENV', default='local')  # opciones: 'local', 'postgres', 'supabase'

if ENV == 'postgres':
    DATABASES['default'] = DATABASES['postgres_local']
elif ENV == 'supabase':
    DATABASES['default'] = DATABASES['supabase']
else:
    DATABASES['default'] = DATABASES['local_sqlite']

# -----------------------------
# Validación de contraseñas
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------------
# Internacionalización
# -----------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -----------------------------
# Archivos estáticos
# -----------------------------
STATIC_URL = 'static/'

# -----------------------------
# Auto field por defecto
# -----------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
