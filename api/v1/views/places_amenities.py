#!/usr/bin/python3
'''
Module places_amenities

implements view  methods


'''
from api.v1.views import app_views
from models import storage
from flask import abort, request, jsonify
from models.place import Place
from models.amenity import Amenity
import os

STORAGE_TYPE = os.getenv('HBNB_TYPE_STORAGE')

app_views.route('/places/<place_id>/amenities', strict_slashes=False, methods=['GET'])
def get_amenity_of_place(place_id):
    '''retrieve'''
    if STORAGE_TYPE == 'db':
        place = storage.get(Place, place_id)
        if place is None:
            abort(404)
        amenities = [amenity.to_dict() for amenity in place.amenities]
    else:
        place = storage.get(Place, place_id)
        if place is None:
            abort(404)
        amenities = [storage.get(Amenity, amenity_id).to_dict() for amenity_id in place.amenity_ids]
    return jsonify(amenities)

    
