from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablenaame__ = 'Data'
    ID = db.Column('ID', db.Integer,  primary_key=True)
    name = db.Column("name", db.String(100), nullable=False)
    latitude = db.Column("latitude", db.Numeric(40), nullable=True)
    longitude = db.Column("longitude", db.Numeric(40), nullable=True)
