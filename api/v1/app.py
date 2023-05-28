from flask import  Flask
from models import storage
from api.v1.views import app_views
import os
HOST = os.environ.get('HBNB_API_HOST')
PORT = os.environ.get('HBNB_API_PORT')

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def cloz():
    '''display route / hello HBNB!'''
    storage.close()

# @app.errorhandler(404)
# def page_not_found():
#     '''
#     handler for 404 errors'''
#     return jsonify(error='Not found'), 404

if __name__ == '__main__':
    app.run(debug = True, host=HOST, port=PORT, threaded=True)
