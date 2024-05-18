from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base

class Productos(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(300), unique=True, nullable=False)
    unidad_medida = Column(String(3), unique=False, nullable=False)
    cantidad_stock = Column(Integer, unique=False, nullable=False)
    valor_unitario = Column(Float(10,8))
    categoria = Column(Integer, ForeignKey('categorias.id'),nullable=False)
    
    def __init__(self,descripcion,unidad_medida,cantidad_stock,valor_unitario,categoria):
      self.descripcion = descripcion
      self.unidad_medida = unidad_medida
      self.cantidad_stock = cantidad_stock
      self.valor_unitario = valor_unitario
      self.categoria = categoria
    
    def agregar_producto(producto):
      producto = session.add(producto)
      session.commit()
      return producto
    
    def obtener_productos():
      productos = session.query(Productos).all()
      return productos    