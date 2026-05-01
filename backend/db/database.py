from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import DATABASE_URL

# Create DB engine (connection)
engine = create_engine(DATABASE_URL)

# Create session (used for DB operations)
SessionLocal = sessionmaker(bind=engine)

# Base class for models
Base = declarative_base()