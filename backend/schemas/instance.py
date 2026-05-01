from pydantic import BaseModel, ConfigDict


# Input schema
class InstanceCreate(BaseModel):
    instance_name: str
    instance_id: str
    instance_type: str


# Action schema (for start/stop)
class InstanceAction(BaseModel):
    instance_id: str


# Output schema
class InstanceResponse(BaseModel):
    id: int
    instance_name: str
    instance_id: str
    instance_type: str

    model_config = ConfigDict(from_attributes=True)