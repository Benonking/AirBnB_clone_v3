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

app_views.route('/places/<place_id>/amenities', strict_slashes=False, methods=['GET'])
def get_amenity_of_place(place_id):
    '''retrieve'''
    
    places = storage.get(Place, place_id)
    
