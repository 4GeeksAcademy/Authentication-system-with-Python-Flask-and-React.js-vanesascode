"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException

# pipenv install flask-jwt-extended

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

api = Blueprint('api', __name__)

################# AUTHENTICATION ###############################https://www.youtube.com/watch?v=8-W2O_R95Pk

# 1 -  Create a token (generate the JWT)

# 2 -  Storing that token

# 3 -  Requesting using that token from that moment on


############################################################################################################

# 1 -  Create a token (generate the JWT, and save it in the .env file!):


# Create a route to authenticate your users and return JWTs(login) The
# create_access_token() function is used to actually generate the JWT.
@api.route("/token", methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test" or password != "test":
        return jsonify({"msg": "Bad email or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)


# Thanks to the @jwt_required() decorator, only people with token can access
@api.route("/hello", methods=["GET"])
@jwt_required() 
def get_hello():
    email = get_jwt_identity()
    dictionary = {
    "message": "This is your private message: Hello World " + email + "!!!"
    }
    return jsonify(dictionary)