from flask import request, jsonify

from . import bp
from app.models import Marvel, User
from app.blueprints.api.helpers import token_required

@bp.get('/heroes')
@token_required
def api_heroes(user):
    result = []
    heroes = Marvel.query.all()
    for hero in heroes:
        result.append({
            'id':hero.id,
            'name':hero.name, 
            'description':hero.description, 
            'hero':hero.user_id
            })
    return jsonify(result), 200

# Recieve Posts from Single User
@bp.get('/heroes/<username>')
@token_required
def hero_posts(user, username):
    user = User.query.filter_by(username=username).first()
    if user:
      return jsonify([{
            'id':hero.id,
            'name':hero.name, 
            'description':hero.description, 
            'hero':hero.user_id
              } for hero in user.marvel_char]), 200
    return jsonify([{'message':'Invalid Username'}]), 404 

# Send single post
@bp.get('/hero/<mar_id>')
@token_required
def get_post(user, mar_id):
    try:
      hero = Marvel.query.get(mar_id)
      return jsonify([{
            'id':hero.id,
            'name':hero.name, 
            'description':hero.description, 
            'hero':hero.user_id
              }])
    except: 
      return jsonify([{'message':'Invalid Post Id'}]), 404

# Make a Post
@bp.post('/hero')
@token_required
def make_post(user):
    try:
#  Recieve their post data
        content = request.json
        marv = Marvel(description=content.get('description'),user_id=user.user_id)

        marv.commit()
  
        return jsonify([{'message':'Post Created','description':marv.description}])
    except:
       jsonify([{'message':'invalid form data'}]), 401