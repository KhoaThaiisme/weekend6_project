from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_required
from . import bp

from app.models import User, Marvel
from app.forms import MarvelForm

@bp.route('/hero', methods=['GET', 'POST'])
@login_required
def hero():
    form = MarvelForm()
    if form.validate_on_submit():
        m = Marvel(
            name=form.name.data, 
            description=form.description.data,
            comic_appeared_in=form.comic_appeared_in.data,
            super_powers=form.super_powers.data
        )
        m.user_id=current_user.user_id
        m.commit()
        flash('Turned into')
        return redirect(url_for('marvel.user_page', username=current_user.username))
    return render_template('hero.j2', form=form)

@bp.route('/userpage/<username>')
@login_required
def user_page(username):
    user = User.query.filter_by(username=username).first()
    return render_template('user_page.j2', title=username, user=user)