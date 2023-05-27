from models import storage
from api.v1.views import app_views
from flask import jsonify, abort

@app_views.route('states', methods=['GET'])
def states():
    '''retrive all state obj'''
    try:
        States = storage.all(State)
        stateList = []
        for s in states:
            stateList.append(States[s].to_dict())
        return jsonify(stateList)
    except:
        abort(404)
