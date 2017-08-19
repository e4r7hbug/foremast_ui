"""Main FAL.S.Y application."""
import pathlib

from falsy.falsy import FALSY

STATIC_DIR = pathlib.Path(__file__).parent / 'static'
API_FILE = STATIC_DIR / 'v1.yml'

APP = FALSY(static_dir=str(STATIC_DIR))
APP.swagger(str(API_FILE), theme='impress')

API = APP.api
