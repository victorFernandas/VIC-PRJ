'''
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker





DATABASE_URL = 'sqlite:///.task.db'

# Engine created:

engine = create_engine(DATABASE_URL, connect_args = {'check_same_thread': False})

#Declarative mapping:

Base = declarative_base()

#Define session:

SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind=engine)

#Task Modal:

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key= True, index= True)
    title = Column(String, index= True)
    description = Column (String, index= True)

Base.metadata.create_all(bind=engine)
'''


# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Format: postgresql://username:password@host:port/database_name
DATABASE_URL = "postgresql://postgres:victor@localhost:5432/vehicle_management"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency for getting DB session in routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

