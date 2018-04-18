from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from database.model import db

dbapp = Flask(__name__)

manager = Manager(dbapp)
migrate = Migrate(dbapp, db)

dbapp.config['SQLALCHEMY_DATABASE_URI'] =
'postgresql://postgres:test123@127.0.0.1:5432/post'

dbapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

manager.add_command('db', MigrateCommand)

db.init_app(dbapp)

if __name__ == '__main__':
    manager.run()
