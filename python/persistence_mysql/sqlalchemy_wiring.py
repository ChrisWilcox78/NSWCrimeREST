from os import environ
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

DEFAULT_MYSQL_USER = "crimes"
DEFAULT_MYSQL_USER_PW = "abc123"
DEFAULT_MYSQL_HOST = "localhost"
DEFAULT_MYSQL_PORT = "3306"


def get_engine():
    host = environ.get("CRIMES_MYSQL_HOST", DEFAULT_MYSQL_HOST)
    port = environ.get("CRIMES_MYSQL_PORT", DEFAULT_MYSQL_PORT)
    user = environ.get("CRIMES_MYSQL_USER", DEFAULT_MYSQL_USER)
    pw = environ.get("CRIMES_MYSQL_USER_PW", DEFAULT_MYSQL_USER_PW)
    return create_engine(
        "mysql+mysqlconnector://" + user + ":" + pw + "@" + host + ":" + port + "/crime_reports")


def get_session():
    engine = get_engine()
    Base.metadata.bind = engine
    return sessionmaker(bind=engine)()
