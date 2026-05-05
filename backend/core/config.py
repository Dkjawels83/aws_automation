from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()


# ========================
# DATABASE CONFIG
# ========================
DATABASE_URL = os.getenv("DATABASE_URL")


AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")