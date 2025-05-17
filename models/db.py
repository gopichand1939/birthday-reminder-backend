import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get MongoDB URI from environment variable
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["birthdayDB"]
collection = db["birthdays"]
