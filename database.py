from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_dATABASE = 'postgresql://postgress:24865050!@localhost:5432/QuizDB'

engine = create_engine(URL_dATABASE)

session_local = sessionmaker(autocommit = False,autoflush = False,bind = engine)

Base = declarative_base()