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
    # What we send from the login form, by separate: 

    # email = request.json.get("email", None)
    # password = request.json.get("password", None)

    # What we send from the login form, altogether:
    body = request.get_json()

    # if body is None:
    #     raise APIException(
    #         "You need to specify the request body as a json object", status_code=400)

    if body is None: 
        return jsonify({"msg": "Body missing"}), 400
    if "email" not in body:
        return jsonify({"msg": "Email missing"}), 400
    if "password" not in body:
        return jsonify({"msg": "password missing"}), 400
    
    user = User.query.filter_by(email=body["email"], password=body["password"]).first()
    if user is None: 
        return jsonify({"msg": "user doesn't exist"})
    access_token = create_access_token(identity=user.email)
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


# GET ALL USERS:

@api.route('/user', methods=['GET'])
def get_users():
    users = User.query.all()

    if not users:
        return jsonify(message="No users found"), 404

    all_users = list(map(lambda x: x.serialize(), users))
    return jsonify(message="Users", users=all_users), 200

# REGISTER USER: 

@api.route('/user', methods=['POST'])
def add_new_user():
    request_body_user = request.get_json()

    new_user = User(email=request_body_user["email"], password=request_body_user["password"], is_active=request_body_user["is_active"])
    db.session.add(new_user)
    db.session.commit()

    return jsonify(request_body_user), 200

# GET ONE USER BY EMAIL?????:

@api.route('/user/<int:user_email>', methods=['GET'])
def get_user(user_email):
    user = User.query.get(user_email)

    if not user:
        return jsonify({'message': 'User not found'}), 404

    serialized_user = user.serialize()
    return jsonify({'user': serialized_user}), 200