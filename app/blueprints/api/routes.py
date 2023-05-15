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
            'id':heroes.id,
            'name':heroes.name, 
            'description':heroes.description, 
            'hero':heroes.user_id
            })
    return jsonify(result), 200

# Recieve Posts from Single User
@bp.get('/heroes/<username>')
@token_required
def hero_posts(user, username):
    user = User.query.filter_by(username=username).first()
    if user:
      return jsonify([{
            'id':heroes.id,
            'name':heroes.name, 
            'description':heroes.description, 
            'hero':heroes.user_id
              } for heroes in user.marvel_char]), 200
    return jsonify([{'message':'Invalid Username'}]), 404 

# Send single post
@bp.get('/hero/<hero_id>')
@token_required
def get_post(user, mar_id):
    try:
      heroes = Marvel.query.get(mar_id)
      return jsonify([{
            'id':heroes.id,
            'name':heroes.name, 
            'description':heroes.description, 
            'hero':heroes.user_id
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
    #  Create a post instance or entry
    #  Add foreign key to user id
        post = Marvel(description=content.get('description'),user_id=user.user_id)
    # commit our post
        post.commit()
    #  return message
        return jsonify([{'message':'Post Created','body':post.body}])
    except:
       jsonify([{'message':'invalid form data'}]), 401