from flask import Blueprint
from .model import *

database = Blueprint('database', __name__)
