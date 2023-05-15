from flask import render_template

from . import bp

@bp.route('/')
def home():
    return render_template(
        'index.j2',
        title="Welcome to Marvelous"
    )

# @bp.route('/about')