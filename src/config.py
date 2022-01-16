import os
from pathlib import Path

from dotenv import load_dotenv

dotenv_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path)


def check_path(path):
    return str(path) if path.exists() else ''


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DATA_PATH = Path(__file__).parent.parent.parent / 'data'
