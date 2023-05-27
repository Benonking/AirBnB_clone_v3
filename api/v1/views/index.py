from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status(app_view):
    ''' returns a string that reports a ststus ok'''
    
    return jsonify({'status': 'OK'})

# @app_views.route('/api/v1/stats', strict_slashes=False)
# def stats():
#     '''
#     Retriieve the number of obj instances'''
#     if STORAGE_TYPE == 'db':
#         classes = ["Amenity", 'City', 'Place', 'Review', 'State', 'User']
#     else:
#         classes = [Amenity, City, Place, Review, State, User]
#     tb_name = ["amenities", 'cities', 'places', 'reviews', 'states', 'users']
#     num = {}
#     for i in range(len(classes)):
#         num[tb_name[i]] == storage.count(classes)
#     return jsonify(num)
