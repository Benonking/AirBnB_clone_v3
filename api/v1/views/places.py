#!/usr/bin/python3
'''
Module places
implement methods:
        create_palce
        update_place
        get_place
        get_places
'''
from api.v1.views import app_views
from flask import abort, request, jsonify
from models.place import Place
from models.city import City
from models.user import User
from models import storage

@app_views.route('/cities/<city_id>/places', strict_slashes=False, methods=['GET'])
def get_places(city_id):
    '''
    retrieve all place objects
    '''
    city = storage.get(City, city_id)
    if city is None:
        abort(404)

    places = [place.to_dict() for place in city.places]
    return jsonify(places)

@app_views.route('/places/place_id', strict_slashes=False, methods=['GET'])
def get_place(place_id):
    '''
    get place given id
    '''
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())

@app_views.route('/places/place_id', strict_slashes=False, methods=['DELETE'])
def delete_place(place_id):
    '''
    delete a place given place_id
    '''
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    place.delete()
    storage.save()
    return jsonify({}), 200

@app_views.route('/cities/<city_id>/places', strict_slashes=False, methods=['POST'])
def create_place(city_id):
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    elif 'name' not in request.get_json():
        return jsonify({'error': 'Missing name'}), 400
    elif 'user_id' not in request.get_json():
        return jsonify({'error': 'Missing user_id'}), 400
    else:
        dt = request.get_json()
        city = storage.get(City, city_id)
        user = storage.get(User, dt['user_id'])
        if city is None or user is None:
            abort(404)
        dt['city_id'] = city_id
        dt['user_id'] = user.id
        obj = Place(**dt)
        obj.save()
        return jsonify(obj.to_dict()), 201

@app_views.route('/places/<place_id>', strict_slashes=False, methods=['PUT'])
def update_place(place_id):
    place = storage.get(Place, place_id)
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    ignore = ('id', 'created_at', 'updated_at', 'user_id', 'city_id')
    dt = request.get_json()
    for k in dt.keys():
        if k in ignore:
            pass
        else:
            setattr(place, k, dt[k])
    place.save()
    return jsonify(place.to_dict()), 200

 