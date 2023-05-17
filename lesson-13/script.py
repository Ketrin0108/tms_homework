from dotenv import load_dotenv
import os

load_dotenv()
print(f"ENV {os.environ.get('ENV')}")
