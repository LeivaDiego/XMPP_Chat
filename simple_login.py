import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

JID = os.getenv("JID")
PASSWORD = os.getenv("PASSWORD")

print(f"JID: {JID}")
print(f"PASSWORD {PASSWORD}")