from flask import render_template
from database import *

pages = Blueprint('pages', __name__)


@pages.route('/show')
# This will route you to user location and their names + other sensed data
# I think it should be merged with the dashboard.
def show_map():
    entries = {"lat": 24.7140015, 'lng': 46.6415485}
    return render_template('showmap.html', data=entries)


''' It will show the traffic of user as heat map '''


@pages.route('/show_heat')
def show_heat():
    users = User.query.with_entities(User.latitude, User.longitude)
    data = [[float(x[0]), float(x[1])] for x in users]
    return render_template('heatmap.html', data=data)


'''The admin dashboard, where it will show the user data'''


@pages.route('/dashboard')
def dashboard():
    users = User.query.with_entities(User.latitude, User.longitude)
    data = [[float(x[0]), float(x[1])] for x in users]
    return render_template('dashboard.html', data=data)
