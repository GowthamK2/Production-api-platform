from app.database import engine
from app.database import Base

def init_db():
    Base.metadata.create_all(bind=engine)