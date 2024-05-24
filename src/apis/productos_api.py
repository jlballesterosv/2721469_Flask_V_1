from flask_restful import Resource
from flask import request

from src.models.productos import Productos

class ProductosApi(Resource):
    def get(self):
       return "hola mundo" 
   
    def post(self):
        producto = Productos(descripcion=request.json['descripcion']
                             , valor_unitario=request.json['valor_unitario']
                             ,unidad_medida=request.json['unidad_medida']
                             ,cantidad_stock=request.json['cantidad_stock']
                             ,categoria=request.json['categoria'])
        try:
            Productos.agregar_producto(producto)
        except Exception:
            return "Error: Producto repetido", 409
        return "Producto almacenado correctamente"