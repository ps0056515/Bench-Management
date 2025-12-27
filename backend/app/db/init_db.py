from app.db.session import engine
from app.db.base import Base
import app.models  # IMPORTANT

def init_db():
    Base.metadata.create_all(bind=engine)
