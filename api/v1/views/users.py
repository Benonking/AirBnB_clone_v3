#!/usr/bin/python3
'''
Module User
implement methods create, update, delete, retrieve on user objscts
'''
from models import storage
from models.user import User
from api.v1.views import app_views
from flask import jsonify, abort, request

@app_views.route('/users', strict_slashes=False, methods=['GET'])
def get_users():
    '''
    retrieve all users
    '''
    userList = [user.to_dict() for user in storage.all('User').values()]
    return jsonify(userList)

@app_views.route('/users/<user_id>', strict_slashes=False, methods=['GET'])
def get_user(user_id):
    '''
    retrieve a user given user.id
    '''
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return(user.to_dict())

@app_views.route('users/<user_id>', strict_slashes=False, methods=['DELETE'])
def delete_user(user_id):
    '''
    delete user
    '''
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    user.delete()
    storage.save()
    return jsonify({}), 200

@app_views.route('/users', strict_slashes=False, methods=['POST'])
def create_user():
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    elif 'email' not in request.get_json():
        return jsonify({'error': 'Missing email'}), 400
    elif 'password' not in request.get_json():
        return jsonify({'error': 'Missing password'}), 400
    else:
        dt = request.get_json()
        user = User(**dt)
        storage.save()
    return jsonify(user.to_dict()), 201

@app_views.route('/users/<user_id>', strict_slashes=False, methods=['PUT'])
def update_user(user_id):
    '''
    update user
    '''
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    dt = request.get_json()
    ignore = ('id', 'email', 'create_at', 'update_at')
    for k in dt.keys():
        if k in ignore:
            pass
        else:
            setattr(user, k, dt[k])
    user.save()
    return jsonify(user.to_dict()), 200


