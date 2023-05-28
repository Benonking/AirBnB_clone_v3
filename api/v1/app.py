from flask import  Flask, jsonify
from models import storage
from api.v1.views import app_views
import os, json
HOST = os.environ.get('HBNB_API_HOST')
PORT = os.environ.get('HBNB_API_PORT')

app = Flask(__name__)
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
    return jsonify(error='Not found'), 404

if __name__ == '__main__':
    if HOST and PORT:
        app.run(host=HOST, port=PORT, debug=True, threaded=True)
    else:
        app.run(debug = True, host='0.0.0.0', port='5000', threaded=True)
