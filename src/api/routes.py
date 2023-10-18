"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
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
    dictionary = {
    "message": " " + email 
    }
    return jsonify(dictionary)


# GET ALL USERS:

@api.route('/user', methods=['GET'])
def get_users():
    users = User.query.all()

    if not users:
        return jsonify(message="No users found"), 404

    all_users = list(map(lambda x: x.serialize(), users))
    return jsonify(message="Users", users=all_users), 200



