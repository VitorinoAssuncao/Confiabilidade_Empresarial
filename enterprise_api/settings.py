import os
from dotenv import load_dotenv

_dotenv_name = '.env.'
os.environ['FLASK_ENV'] = 'development'
_env = os.getenv('FLASK_ENV')
_dotenv_file = os.path.join(os.path.dirname(__file__),_dotenv_name + _env.lower())

load_dotenv(dotenv_path=_dotenv_file,verbose=True)

FLASK_APP = 'run'
FLASK_ENV = _env
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS',True)
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DEBUG = os.getenv('DEBUG',True)
SECRET_KEY = os.getenv('SECRET_KEY')