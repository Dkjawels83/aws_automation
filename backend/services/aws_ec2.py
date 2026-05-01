import boto3
from core.config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION

# Create EC2 client
ec2_client = boto3.client(
    "ec2",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)


def start_instance(instance_id: str):
    try:
        response = ec2_client.describe_instances(InstanceIds=[instance_id])
    

        reservations = response.get("Reservations")

        if not reservations:
            return {"error": "Instance not found"}

        instance = reservations[0]["Instances"][0]
        state = instance["State"]["Name"]

        # If already running
        if state == "running":
            return {"message": "Instance already running"}

        # If already starting
        if state == "pending":
            return {"message": "Instance is already starting"}

        # Start instance
        ec2_client.start_instances(InstanceIds=[instance_id])

        return {"message": "Instance starting"}

    except Exception as e:
        return {"error": str(e)}