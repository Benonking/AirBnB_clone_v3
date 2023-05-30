#!/usr/bin/python3
'''
Module app
This is a flask application 
    implements bluesprints for diferent app views
'''
from flask import  Flask, jsonify, make_response
from models import storage
from flask_cors import CORS
from api.v1.views import app_views
import os
HOST = os.environ.get('HBNB_API_HOST')
PORT = os.environ.get('HBNB_API_PORT')

app = Flask(__name__)
CORS(app, origins='0.0.0.0')
app.register_blueprint(app_views)

@app.teardown_appcontext
def cloz(exec):
    '''display route / hello HBNB!'''
    storage.close()

@app.errorhandler(404)
def page_not_found(e):
    '''
     handler for 404 errors'''
    #err = {'eror': 'Not found'}
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    if HOST and PORT:
        app.run(host=HOST, port=PORT, debug=True, threaded=True)
    else:
        app.run(debug = True, host='0.0.0.0', port='5000', threaded=True)
