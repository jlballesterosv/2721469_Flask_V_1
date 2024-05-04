from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///facturacion.db'

db = SQLAlchemy(app)

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(300), unique=True, nullable=False)
    unidad_medida = db.Column(db.String(3), unique=False, nullable=False)
    cantidad_stock = db.Column(db.Integer, unique=False, nullable=False)
    precio = db.Column(db.Integer, unique=False, nullable=False)
    
class Clientes(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)    
    nombre = db.Column(db.String(100), unique=False, nullable=False)
    tipo_identificacion = db.Column(db.String(20), unique=False, nullable=False)
    numero_identificacion = db.Column(db.String(20), unique=True, nullable=False)
    direccion = db.Column(db.String(300), unique=False, nullable=False)
    telefono = db.Column(db.String(20), unique=False, nullable=False)
    
with app.app_context():
    db.create_all()

from controllers import *

if __name__ == '__main___':
    app.run(debug=True)