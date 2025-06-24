from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

# connection Db
SQLALCHEMY_DB_URL = "postgresql://be_project_caffe_user:N8U3aPImCusr0ECxQHNzc8BX7FcU1zJ0@dpg-d1d4fe7diees73cg1omg-a.oregon-postgres.render.com/be_project_caffe"
engine = create_engine(SQLALCHEMY_DB_URL) 
SessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base = declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db 
    finally:
        db.close()
def create_table():
    Base.metadata.create_all(bind=engine)
