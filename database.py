from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# for postgresql test locally
'''host_server = os.environ.get('host_server', 'localhost')
db_server_port = urllib.parse.quote_plus(
    str(os.environ.get('db_server_port', '8081')))
database_name = os.environ.get('database_name', 'memes')
db_username = urllib.parse.quote_plus(
    str(os.environ.get('db_username', 'postgres')))
db_password = urllib.parse.quote_plus(
    str(os.environ.get('db_password', 'ishan')))
ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode', 'prefer')))
SQLALCHEMY_DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(
    db_username, db_password, host_server, db_server_port, database_name, ssl_mode)'''


# Test Database

SQLALCHEMY_DATABASE_URL = "sqlite:///./memes.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Original Database
'''
SQLALCHEMY_DATABASE_URL = ""
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_size=3, max_overflow=0
)'''


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()