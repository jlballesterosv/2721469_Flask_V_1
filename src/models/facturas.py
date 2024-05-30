from sqlalchemy import Column, Integer, DateTime, ForeignKey
from src.models import session, Base

class Facturas(Base):
    __tablename__ = "facturas"
    id = Column(Integer, primary_key=True)
    fecha = Column(DateTime, nullable=False)
    cliente = Column(Integer, ForeignKey('clientes.id'), nullable=False)   
    
    def __init__(self,fecha,cliente):
      self.fecha = fecha
      self.cliente = cliente
    
    def agregar_factura(factura):
      factura = session.add(factura)
      session.commit()
      return factura
    
    def obtener_facturas():
      factura = session.query(Facturas).all()
      return factura