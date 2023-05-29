#!/usr/bin/python3
'''
modeule amenities
impliment   create, update, delete on amenity objects
'''
from models.amenity import Amenity
from models import storage
from api.v1.views import app_views
from flask import jsonify, abort, request

@app_views.route('/amenities', strict_slashes=False, methods=['GET'])
def get_amenities():
    '''
    retrieve all amnities objects
    '''
    amenityList = [amenity.to_dict() for amenity in storage.all('Amenity').values()]
    return jsonify(amenityList)

@app_views.route('/amenities/<amenity_id>', strict_slashes=False, methods=['GET'])
def get_amneityID(amenity_id):
    '''
    get a amnrity object (give ID)
    '''
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())

@app_views.route('/amenities/<amenity_id>', strict_slashes=False, methods=['GET'])
def delete(amenity_id):
    '''
    delete amnity object
    '''
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    amenity.delete()
    storage.save()
    return jsonify({}), 200
@app_views.route('/amenities', strict_slashes=False, methods=['POST'])
def create_amenity():
    '''
    create amenity
    '''
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    elif 'name' not in request.get_json():
        return jsonify({{'error': 'Missing name'}}), 400
    
    else:
        dt = request.get_json()
        inst = Amenity(**dt)
        inst.save()
    return jsonify(inst.to_dict()), 201

@app_views.route('/amenities/<amenity_id>', strict_slashes=False, methods=['PUT'])
def update_amenity(amenity_id):
    '''
    update amenity
    '''
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)

    dt  = request.get_json()
    amenity.name=dt['name']
    amenity.save()
    return jsonify(amenity.to_dict()), 200

