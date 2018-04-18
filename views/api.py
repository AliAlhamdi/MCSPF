from flask import request, jsonify
from database import *
from settings.crypto import load_pu_key

api = Blueprint('api', __name__)


@api.route('/data', methods=['POST'])
def data_():
    if not request.json:
        return jsonify("the request is not json ")
    data = request.get_json()
    insert = User(name=str(data["data"][0]['name']),
                  latitude=float(data["data"][1]['latitude']),
                  longitude=float(data["data"][2]['longitude']))
    db.session.add(insert)
    db.session.commit()
    return jsonify("HI")


@api.route('/public_key', methods=['GET'])
def public_key():
    key = load_pu_key()
    # data = {"key": key}
    return key
