from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# os.environ['DB_USER'] = "postgres"
# os.environ['DB_PASSWORD'] = "1234"
# os.environ['DB_HOST'] = "localhost"
# os.environ['DB_PORT'] = "5432"
# os.environ['DB_NAME'] = "postgres"

SQLALCHEMY_DATABASE_URL = f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}" \
                          f":{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print('456')
Base = declarative_base()
