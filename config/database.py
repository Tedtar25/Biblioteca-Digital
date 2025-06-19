import os 
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name = "../database.sqlite"

#Estamos leyendo el archivo de la base de datos desde la carpeta config
base_dir = os.path.dirname(os.path.realpath(__file__))

#creamos la url de la base de datos uniendo las 2 variables anteriores
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

engine = create_engine(database_url, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()