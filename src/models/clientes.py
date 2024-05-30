from sqlalchemy import Column, Integer, String
from src.models import Base,session
from sqlalchemy_serializer import SerializerMixin


class Clientes(Base, SerializerMixin):
    __tablename__ = "clientes"    
    id = Column(Integer, primary_key=True)    
    nombre = Column(String(100), unique=False, nullable=False)
    tipo_identificacion = Column(String(20), unique=False, nullable=False)
    numero_identificacion = Column(String(20), unique=True, nullable=False)
    direccion = Column(String(300), unique=False, nullable=False)
    telefono = Column(String(20), unique=False, nullable=False)
    
    
    def __init__(self,nombre,tipo_identificacion,numero_identificacion,direccion,telefono):
      self.nombre = nombre
      self.tipo_identificacion = tipo_identificacion
      self.numero_identificacion = numero_identificacion
      self.direccion = direccion
      self.telefono = telefono
    
    def agregar_cliente(cliente):
      cliente = session.add(cliente)
      session.commit()
      return cliente
    
    def obtener_clientes():
      clientes = session.query(Clientes).all()
      return clientes
    
    def obtener_cliente_por_id(id):
      cliente = session.query(Clientes).get(id)
      return cliente.to_dict()