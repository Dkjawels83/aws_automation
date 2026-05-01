from sqlalchemy import Column, Integer, String
from db.database import Base

class Instance(Base):
    __tablename__ = "instances"

    id = Column(Integer, primary_key=True, index=True)
    instance_name = Column(String, nullable=False)
    instance_id = Column(String, nullable=False)
    instance_type = Column(String, nullable=False)