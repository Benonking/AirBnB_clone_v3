from models.amenity import Amenity
from models import storage
from api.v1.views import app_views
from flask import jsonify, abort, request

@app_views('/amenities', strict_slashes=False, methods=['GET'])
def get_amenities():
    '''
    
    '''