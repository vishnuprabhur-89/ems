from flask import request, Blueprint, jsonify, make_response, json
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import hashlib  # hash the user password
from bson import json_util
from model.app import UserManagement

API = Blueprint('controller', __name__)
data_base = UserManagement()

@API.route('/register', methods=['POST'])
def register():
    collection = data_base.user_auth()
    new_user = request.get_json()
    new_user['password'] = hashlib.sha256(new_user['password'].encode('utf-8')).hexdigest()
    userExists = collection.find_one({"username": new_user['username']})
    if userExists is None:
        try:
            print(new_user)
            status = collection.insert_one(new_user)
            return jsonify({'message': 'New user acccount created successfully.'}), 200
        except Exception as e:
            print(e)
            return jsonify({'message': 'Send proper values'}), 400
    else:
        return jsonify({'message': 'Username is already exists.'}), 409


@API.route('/login', methods=['POST'])
def login():
    collection = data_base.user_auth()
    user_info = request.get_json()
    isUserExists = collection.find_one({'username': user_info['username']})
    if isUserExists:
        encrypted_password = hashlib.sha256(
            user_info['password'].encode('utf-8')).hexdigest()
        if encrypted_password == isUserExists['password']:
            access_token = create_access_token(
                identity=isUserExists['username'])
            return jsonify(access_token=access_token, user_role=isUserExists['role']), 200
        else:
            return jsonify({'message': 'Password is incorrect'}), 401
    else:
        return jsonify({'message': 'Username is incorrect'}), 401


@API.route('/create/profile',  methods=['POST'])
@jwt_required()
def createUserProfile():
    current_user = get_jwt_identity()  # Get the identity of the current user
    collection = data_base.user_details()
    user_info = request.get_json()
    user_info['user_name'] = current_user
    user_profile_exists = collection.find_one(
        {"user_name": {"$in": [current_user]}})
    if user_profile_exists is None:
        collection.insert_one(user_info)
        return jsonify({'message': "profile created successfully"}), 200
    else:
        return make_response(jsonify({'message': "profile already exists"}), 409)


@API.route('/update/profile', methods=['PUT', 'DELETE'])
@jwt_required()
def updateProfile():
    current_user = get_jwt_identity()  # Get the identity of the current user
    collection = data_base.user_details()

    if request.method == "PUT":
        result = collection.update_one({'user_name': current_user},
                                       {"$set": request.get_json()})
        return make_response(result.raw_result)
    elif request.method == "DELETE":
        result = collection.delete_one({'user_name': current_user})
        return make_response(result.raw_result)

@API.route('/get/profile', methods=['GET'])
@jwt_required()
def getProfile():
    current_user = get_jwt_identity()
    collection = data_base.user_details()
    result = collection.find_one({"user_name": current_user})
    if result is not None:
        return json.loads(json_util.dumps(result))
    else:
        return jsonify({'message': 'Profile not exists'})