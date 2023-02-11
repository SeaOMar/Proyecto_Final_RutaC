from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False) 
    nombre = db.Column(db.String(20), nullable=True)
    raza = db.Column(db.String(20), nullable=True)
    fecha = db.Column(db.String(20), nullable=False)
    full_name = db.Column(db.String(20), nullable=True)
    DNI = db.Column(db.String(20), nullable=True)
    
