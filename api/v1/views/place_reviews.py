#!/usr/bin/python3
'''
Module review
Implements methods for blue print view review
            create_review
            update_review
            retrieve_review
            delete_review
            get_review
            get_reviews
'''
from models.review import Review
from flask import jsonify, abort, request
from models import storage
from models.place import Place
from models.user import User
from api.v1.views import app_views

@app_views.route('/places/<place_id>/reviews', strict_slashes=False, methods=['GET'])
def get_reviews(place_id):
    '''retrive all reviews'''
    places = storage.get(Place, place_id)
    if places is None:
        abort(404)
    reviews = [review.to_dict() for review in places.reviews]
    return jsonify(reviews)
@app_views.route('/reviews/review_id', strict_salashes=False, methods=['GET'])
def get_review(review_id):
    '''get review given id'''
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    return jsonify(review.tod_dict())

@app_views.route('reviews/<review_id>', strict_slashes=False, methods=False)
def delete_review(review_id):
    '''delete review given reviewId'''
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    review.delete()
    storage.save()
    return jsonify({}), 200

@app_views.route('/places/<place_id>/reviews', methods=['POST'], strict_slashes=False)
def create_review(place_id):
    
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    elif 'user_id' not in request.get_json():
        return jsonify({'error': 'Missing user_id'}), 400
    elif 'text' not in request.get_json():
        return jsonify({'error': 'Mising text'}), 400
    else:
        dt = request.get_json()
        user = storage.get(User, dt['user_id'])
        place = storage.get(Place, place_id)
        if place is None or user is None:
            abort(404)
        obj = Review(**dt)
        obj.place_id = place_id
        obj.save()
        return jsonify(obj.to_dict()), 201
    
@app_views.route('reviews/<review_id>', strict_slashes=False, methods=['PUT'])
def update_review(review_id):
    '''update review'''
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'})
    ignore = ('id', 'create_at', 'updated_at', 'place_id', 'user_id')
    dt = request.get_json()
    for k in dt.keys():
        if k in ignore:
            pass
        else:
            setattr(review, k, dt[k])
    review.save()
    return jsonify(review.to_dict()), 200
    



    

