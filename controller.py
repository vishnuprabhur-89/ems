from flask import request, Blueprint, jsonify, make_response
from database import EMSinfo
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import hashlib  # hash the user password

mod = Blueprint('controller', __name__)
database = EMSinfo()


@mod.route('/register', methods=['POST'])
def register():
    collection = database.userInfo()
    new_user = request.get_json()
    new_user['password'] = hashlib.sha256(
        new_user['password'].encode('utf-8')).hexdigest()
    userExists = collection.find_one({"username": new_user['username']})
    if userExists is None:
        collection.insert_one(new_user)
        return jsonify({'message': 'New user acccount created successfully.'})
    else:
        return jsonify({'message': 'Username is already exists.'})


@mod.route('/login', methods=['POST'])
def login():
    collection = database.userInfo()
    user_info = request.get_json()
    isUserExists = collection.find_one({'username': user_info['username']})
    if isUserExists:
        encrypted_password = hashlib.sha256(
            user_info['password'].encode('utf-8')).hexdigest()
        if encrypted_password == isUserExists['password']:
            access_token = create_access_token(
                identity=isUserExists['username'])
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({'message': 'Password is incorrect'}), 401
    else:
        return jsonify({'message': 'Username is incorrect'}), 401


@mod.route('/create/profile',  methods=['POST'])
@jwt_required()
def createUserProfile():
    current_user = get_jwt_identity()  # Get the identity of the current user
    collection = database.userProfile()
    user_info = request.get_json()
    user_info['username'] = current_user
    user_profile_exists = collection.find_one(
        {"username": {"$in": [current_user]}})
    print(user_profile_exists)
    if user_profile_exists is None:
        collection.insert_one(user_info)
        return jsonify({'message': "profile created successfully"}), 200
    else:
        return make_response(jsonify({'message': "profile already exists"}), 409)


@mod.route('/update/profile', methods=['PUT', 'DELETE'])
@jwt_required()
def updateProfile():
    current_user = get_jwt_identity()  # Get the identity of the current user
    collection = database.userProfile()
    if request.method == "PUT":
        result = collection.update_one({'username': current_user},
                                       {"$set": request.get_json()})
        return make_response(result.raw_result)
    elif request.method == "DELETE":
        result = collection.delete_one({'username': current_user})
        return make_response(result.raw_result)
