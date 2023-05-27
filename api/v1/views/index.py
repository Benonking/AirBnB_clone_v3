from api.v1.views import app_views
from flask import jsonify

@app_views.route('/ststus', strict_slashes=False)
def status(app_view):
    
    return jsonify({'ststus': 'OK'})