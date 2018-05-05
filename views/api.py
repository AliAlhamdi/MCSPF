from flask import request, jsonify
from database import *
from settings.crypto import load_pu_key
from flask_cors import decorator, cross_origin, CORS
from settings.crypto import *

api = Blueprint('api', __name__)


@api.route('/data', methods=['POST'])
def data_():
    if not request.json:
        return jsonify("the request is not json ")

    data = request.get_json()
    print(data['data'])
    print(type(data['data']))
    en = data['data'].encode('utf-8')
    data['data'] = decrypt(en)
    insert = User(name=str(data['name']),
                  latitude=float(data['latitude']),
                  longitude=float(data['longitude']))
    db.session.add(insert)
    db.session.commit()
    return jsonify("Thank y"), 200


'''API that response the public key '''


@api.route('/public_key', methods=['GET'])
def public_key():
    key = load_pu_key()
    data = {"key": key.decode('ascii')}
    return jsonify(data)

@api.route('/test')
def test():

    cipher = b'FM3HQzGcc7/KchGnegO2mmEAw6NMuBGJzgwWC0P6IG23kSCuxNEd+vAgqc/jCyiY+IVrEXUW2KNHCfj1g94Na3yzKJZ9zVZyUA8qA3lz1n36fojzb+k0P5TdRAzb14MWfZH+afYXsqHtnMn/4ENB0T5FEwdHCShD/7mOh2WARO5CZd3hg1Lz76iTeFPe0nCvKMWZnKbCcQiew2QE1DutzQAZSkdPJOnyiL+C2TcBSt1FlN70Z5f1NORze86i/eE2yuLoOukYgf6PBJMH2f6J0JEdZUcTiaPTG3Z7c/Hc5hp5zn5SwQStLaKxwuI5jQsjHHIeQlIWyDCsPNzOVzVA99pSfeExd1bm7N6acpaT?o5nbezvSPvfNAJ3J55TALPeJJdCmjuNR4NR54UrRVqA='
    print(type(cipher))
    print(cipher)

    print(decrypt(cipher))
    return jsonify("Ali")
