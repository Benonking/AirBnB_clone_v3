from api.v1.views import app_views
import json
from models import city, place, amenity, state, user, storage
import os
STORAGE_TYPE = os.getenv('STORAGE_TYP')
@app_views.route('/status', strict_slashes=False)
def status():
    ''' returns a string that reports a ststus ok'''
    dic = {'status': 'OK'}
    return json.dumps(dic, indent=2)

@app_views.route('/stats', strict_slashes=False)
def stats():
    '''
    Retriieve the number of obj instances'''
    dic = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('Place'),
        'reviews': storage.count('Reviews'),
        'states': storage.count('States'),
        'users': storage.count('User')
    }
    return json.dumps(dic, indent=2)
