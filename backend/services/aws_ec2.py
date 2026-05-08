import boto3
from core.config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION
from utils.otp import generate_otp


termination_otps = {}
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

def stop_instance(instance_id: str):
    try:
        response = ec2_client.describe_instances(InstanceIds=[instance_id])
    

        reservations = response.get("Reservations")

        if not reservations:
            return {"error": "Instance not found"}

        instance = reservations[0]["Instances"][0]
        state = instance["State"]["Name"]
#hia kuch
        # If already running
        if state == "stopped":
            return {"message": "Instance already stopped"}

        # If already starting
        if state == "pending":
            return {"message": "Instance is already stoping"}

        # Start instance
        ec2_client.stop_instances(InstanceIds=[instance_id])

        return {"message": "Instance stoping"}

    except Exception as e:
        return {"error": str(e)}

def reboot_instance(instance_id: str):
    try:
        response = ec2_client.describe_instances(InstanceIds=[instance_id])
        reservations = response.get("Reservations")

        if not reservations:
            return {"error": "Instance not found"}

        instance = reservations[0]["Instances"][0]
        state = instance["State"]["Name"]

        if state == "stoppped":
            return{"message": "Instance is stop"}

        ec2_client.reboot_instances(InstanceIds=[instance_id]) 
        return{"message": "instance is reboot"}

    except Exception as e:
        return{"error":str(e)}

def request_temination(instance_id : str):
    
    otp = generate_otp()

    termination_otps[instance_id]=otp
    print(f"otp store here{otp}")

    return{
        "message":"Otp sent Successfully",
        "otp":otp
    }

def verify_terminate(instance_id: str,otp: str):

    instance_id = instance_id.strip()
    otp = otp.strip()

    print("Received instance_id:", instance_id)
    print("All OTPs:", termination_otps)

    store_otp = termination_otps.get(instance_id)

    print(f"stored otp: {store_otp}")

    if not store_otp:
        return {"error": "No otp found for this"}

    if store_otp != otp:
        return {"error": "Invalid otp"}

    try:
        ec2_client.terminate_instances(
            InstanceIds=[instance_id]
        )

        termination_otps.pop(instance_id, None)

        return {"message": "instance terminating"}

    except Exception as e:
        return {"error": str(e)}