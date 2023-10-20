"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Favs
from api.utils import generate_sitemap, APIException


api = Blueprint('api', __name__)

# pipenv install flask-jwt-extended

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required



################# AUTHORATION ###############################https://www.youtube.com/watch?v=8-W2O_R95Pk

# 1 -  Create a token (generate the JWT)
 
# 2 -  Storing that token ( FLUX line 84)

# 3 -  Requesting using that token from that moment on


############################################################################################################

# 1 -  Create a token (generate the JWT, and save it in the .env file!):


# RETURN PRIVATE MESSAGE ON THE HOME PAGE:


# Thanks to the @jwt_required() decorator, only people with token can access
@api.route("/hello", methods=["GET"])
@jwt_required() 
def get_hello():
    email = get_jwt_identity()
    user = User.query.filter_by(email=email).first()
    name = user.name if user else "Unkown"
    dictionary = {
    "message": " " + name 
    }
    return jsonify(dictionary)


# GET FAVS:

@api.route("/favs/<int:user_id>", methods=['GET'])
def get_favs(user_id):
   favs = Favs.query.filter_by(user_id=user_id).first()
   if not favs:
      return jsonify(message="No favs found"), 404
   return jsonify(favs.serialize()), 200

# POST FAVS:

@api.route("/favs/<int:user_id>", methods=['POST'])
def post_favs(user_id):
   favs = Favs.query.filter_by(user_id=user_id).first()
   if not favs:
      return jsonify(message="No favs found"), 404
   return jsonify(favs.serialize()), 200

# GET ALL USERS:

@api.route('/user', methods=['GET'])
def get_users():
    users = User.query.all()

    if not users:
        return jsonify(message="No users found"), 404

    all_users = list(map(lambda x: x.serialize(), users))
    return jsonify(message="Users", users=all_users), 200



