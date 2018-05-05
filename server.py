from flask import Flask
from views.api import api
from database import database, db
from views.views import pages
from settings.crypto import *
from flask_cors import CORS, cross_origin
app = Flask(__name__)
# CORS(app)
app.register_blueprint(api)
app.register_blueprint(pages)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'postgresql://postgres:test123@127.0.0.1:5432/post'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(database)
db.init_app(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
