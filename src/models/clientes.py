from sqlalchemy import Column, Integer, String
from src.models import Base


class Clientes(Base):
    __tablename__ = "clientes"    
    id = Column(Integer, primary_key=True)    
    nombre = Column(String(100), unique=False, nullable=False)
    tipo_identificacion = Column(String(20), unique=False, nullable=False)
    numero_identificacion = Column(String(20), unique=True, nullable=False)
    direccion = Column(String(300), unique=False, nullable=False)
    telefono = Column(String(20), unique=False, nullable=False)