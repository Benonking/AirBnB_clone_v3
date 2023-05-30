#!/usr/bin/python3
""" A new view for the link between Place objects and Amenity
    objects that handles all default RESTFul API actions """

from models import storage
from models.place import Place
from models.amenity import Amenity
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response


@app_views.route('places/<place_id>/amenities', strict_slashes=False,
                methods=['GET'])
def place_amenities(place_id):
    """Retrieves the list of all Amenity objects of a Place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    if not place.amenities:
        return jsonify([])
    return jsonify([amenity.to_dict() for amenity in place.amenities])


@app_views.route('places/<place_id>/amenities/<amenity_id>',
                strict_slashes=False, methods=['DELETE', 'POST'])
def amenities_in_place(place_id, amenity_id):
    """Manipulates the list of all Amenity objects of a Place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    if request.json == 'DELETE':
        if amenity not in place.amenities:
            abort(404)
        storage.delete(amenity)
        storage.save()
        return make_response(jsonify({}), 200)

    if request.json == 'POST':
        if amenity not in place.amenities:
            place.amenities.append(amenity)
            place.save()
            return make_response(jsonify(amenity.to_dict()), 201)
        return make_response(jsonify(amenity.to_dict()), 200)
