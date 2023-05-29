from models import storage
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State

@app_views.route('/states', strict_slashes=False, methods=['GET'])
def states():
    '''retrive all state objects i json form '''
    stateList = [s.to_dict() for s in storage.all('State'). values()]
    return jsonify(stateList)

@app_views.route('/states/<state_id>', strict_slashes=False, methods=['GET'])
def get_state_id(state_id):
    '''return state id'''
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())

@app_views.route('/states/<state_id>', strict_slashes=False, methods=['DELETE'])
def delete_state(state_id):
    ''' delete state'''
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    state.delete()
    storage.save()
    return jsonify({}), 200

    
      
@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
     '''create state'''
     if not request.get_json():
         return jsonify({"error": "Not a JSON"}), 400
     elif "name" not in request.get_json():
         abort({'error': 'Missing name'}), 400
     else:
         obj_data = request.get_json()
         ins = State(**obj_data)
         ins.save()
     return jsonify(ins.to_dict()), 201

@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
     '''update state'''
     if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
     state = storage.get(State, state_id)
     if state is None:
         abort(404)
     data = request.get_json()
     state.name = data['name']
     state.save()
     return jsonify(state.to_dict()), 200
