from fastapi import FastAPI
from db.database import engine, Base
import db.models  # IMPORTANT
from api.instances import router as post_instance

app = FastAPI()

app.include_router(post_instance)

Base.metadata.create_all(bind=engine)