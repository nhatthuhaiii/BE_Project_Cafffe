from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

# connection Db
SQLALCHEMY_DB_URL = "postgresql://postgres:congnhat@db.wqqrxlmjqbnomzimgopn.supabase.co:5432/postgres"
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
