from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
import pymysql

engine = create_engine("mysql+pymysql://root@localhost/facturacion272146901")
connection = engine.connect()

Base = declarative_base()
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)

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
      session = Session()
      producto = session.add(producto)
      session.commit()
      return producto
    
    def obtener_productos():
      session = Session()
      productos = session.query(Productos).all()
      return productos
      
      
      
      
    
class Categorias(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True)
    categoria  = Column(String(100), unique=True, nullable=False)
    
    def __init__(self,categoria):
      self.categoria = categoria
    
    def obtener_categorias():
      session = Session()
      categorias = session.query(Categorias).all()
      return categorias
  
    
class Clientes(Base):
    __tablename__ = "clientes"    
    id = Column(Integer, primary_key=True)    
    nombre = Column(String(100), unique=False, nullable=False)
    tipo_identificacion = Column(String(20), unique=False, nullable=False)
    numero_identificacion = Column(String(20), unique=True, nullable=False)
    direccion = Column(String(300), unique=False, nullable=False)
    telefono = Column(String(20), unique=False, nullable=False)
    


