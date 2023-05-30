#!/usr/bin/python3
""" A new view for the link between Place objects and Amenity
    objects that handles all default RESTFul API actions """

from models import storage
from models.place import Place
from models.amenity import Amenity
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from os import environ
STORAGE_TYPE = environ.get("HBNB_TYPE_STORAGE")


@app_views.route('places/<place_id>/amenities', strict_slashes=False,
                methods=['GET'])
def place_amenities(place_id):
    """Retrieves the list of all Amenity objects of a Place"""
    place = storage.get(Place, place_id)
    if request.method == 'GET':
        if not place:
            abort(404)
        if STORAGE_TYPE == 'db':
            place_amenities = place.amenities
        else:
            place_amenities_obj = place.amenities
            place_amenities = []
            for amenity in place_amenities_obj:
                response.append(storage.get(Amenity, amenity))
        place_amenities = [
                amen.to_dict() for amen in place_amenities
                ]
        return jsonify(place_amenities)


@app_views.route('places/<place_id>/amenities/<amenity_id>',
                strict_slashes=False, methods=['DELETE', 'POST'])
def amenities_in_place(place_id, amenity_id):
    """Manipulates the list of all Amenity objects of a Place"""
    place = storage.get(Place, place_id)
    amenity = storage.get(Amenity, amenity_id)
    if not amenity or not place:
        abort(404)

    if request.json == 'DELETE':
        if amenity not in place.amenities:
            abort(404)
        if STORAGE_TYPE == 'db':
            place.amenities.remove(amenity)
        else:
            place.amenity_ids.pop(amenity.id, None)
        place.save()
        return make_response(jsonify({}), 200)

    if request.json == 'POST':
        if amenity in place.amenities or amenity.id in place.amenities:
            return make_response(jsonify(amenity.to_dict()), 200)
        if STORAGE_TYPE == 'db':
            place.amenities.append(amenity)
        else:
            place.amenities = amenity
        place.save()
        return make_response(jsonify(amenity.to_dict()), 201)
