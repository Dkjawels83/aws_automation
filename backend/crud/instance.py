from sqlalchemy.orm import Session
from db.models import Instance


def create_instance(db: Session, data):
    instance = Instance(
        instance_name=data.instance_name,
        instance_id=data.instance_id,
        instance_type=data.instance_type
    )

    db.add(instance)        # Add to DB
    db.commit()             # Save permanently
    db.refresh(instance)    # Get updated values (like id)

    return instance