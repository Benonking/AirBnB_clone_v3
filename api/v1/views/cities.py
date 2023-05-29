from models import storage
from models.state import State
from models.city import City
from api.v1.views import app_views
from flask import jsonify, abort, request

@app_views.route('/states/<state_id>/cities', strict_slashes=False, methods=['GET'])
def cities_in_state(state_id):
    '''
    retrieve all city objects of a state
    '''
    state = storage.get(State,state_id)
    if state is None:
        abort(404)
    city_list = [c.to_dict() for c in state.cities]
    return jsonify(city_list), 200

@app_views.route('/cities/<city_id>', strict_slashes=False, methods=['GET'])
def get_city(city_id):
    '''
    Retrieve a city city
    '''
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict()), 200

@app_views.route('/cities/<city_id>', strict_slashes=False, methods=['DELETE'])
def dlelete_city(city_id):
    '''
    delete a city
    '''    
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    city.delete()
    storage.save()
    return jsonify({}), 200

@app_views.route('/states/<state_id>/cities', strict_slashes=False, methods=['POST'])
def create_city(state_id):
    
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    elif 'name' not in request.get_json():
        return jsonify({'error': 'Missing name'}), 400
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    else:
        obj_dt = request.get_json()
        if state is None:
            abort(404)
        obj_dt['state_id'] = state_id
        obj = City(**obj_dt)
        obj.save()
        return jsonify(obj.to_dict()), 201
@app_views.route('/cities/<city_id>', strict_slashes=False, methods=['PUT'])
def update_city(city_id):
    '''update city'''
    if not request.get_json():
      return  jsonify({'error': 'Not a JSON'})
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    dt = request.get_json()
    city.name = dt['name']
    city.save()
    return jsonify(city.to_dict()), 200