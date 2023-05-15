from flask import Blueprint

bp = Blueprint('marvel', __name__, url_prefix='/marvel')

from app.blueprints.marvel import routes