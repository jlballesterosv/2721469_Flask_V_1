from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
import pymysql

engine = create_engine("mysql+pymysql://root@localhost/factura102")
connection = engine.connect()

Base = declarative_base()
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)

session = Session()