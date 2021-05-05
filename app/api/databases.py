

# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker



# # SQLALCHAMY_DATABASE_URL = "mysql+mysqlconnector://root:pranav@localhost:3306/myapi"
# SQLALCHAMY_DATABASE_URL='sqlite:///./newdb.db'

# engine = create_engine(SQLALCHAMY_DATABASE_URL,connect_args={"check_same_thread":False})
# Base=declarative_base()

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import urllib


host_server = os.environ.get('host', '127.0.0.1')
db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port', '5432')))
database_name = os.environ.get('database_name', 'newdb')
db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'postgres')))
db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', 'pranav')))
ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode','prefer')))
SQLALCHEMY_DATABASE_URL  = 'postgresql://{}:{}@{}:{}/{}'.format(db_username, db_password, host_server, db_server_port, database_name)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base=declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
