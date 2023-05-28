from models import storage
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage
from models.state import State

@app_views.route('/states', methods=['GET'])
def states():
    '''retrive all state objects'''
    try:
        States = storage.all(State)
        stateList = []
        for s in States.items():
            stateList.append(States[s].to_dict())
        return jsonify(stateList)
    except:
        abort(404)

# @app_views.route('/states/state_id', methods=['GET'])
# def state_by_id(state_id):
#     try:
#         state = storage.get(State, state_id).to_dict()
#         return jsonify(state)
#     except:
#         abort(404)

# @app_views.route('/api/v1/state_id', methods=['GET'])
# def delete_state(state_id):
#     ''' delete state'''
#     try:
#         storage.delete(State, state_id)
#         storage.save()
#         return {}, 200
#     except:
#         abort(404)
# @app_views.route('/states', methods=['POST'])
# def create_state():
#     '''create state'''
#     dt = request.get_json()
#     if not dt:
#         abort(400, "Not a JSON")
#     if 'name' not in dt:
#         abort(400, 'Missing name')
#     inst = State(dt)
#     inst.save()
#     return jsonify(inst.to_dict()), 201
# @app_views.route('/api/v1/states/state_id')
# def update_state(state_id):
#     st = 'State.' +str(state_id)
#     if k not in storage.all():
#         abort(404)
#         dt = request.get_json()
#     if not dt:
#         abort(400, 'Not a JSON')
#     for k, v in dt.items():
#         if k not in ['id', 'created_at', 'updated_at']:
#             setattr(storage.all()[st], k, v)
#     storage.all()[st].save()
#     return jsonify(storage.get(State, state_id).to_dict()), 200