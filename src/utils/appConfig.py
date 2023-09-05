import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access environment variables and assign them as global variables


ACCOUNT_OVERVIEW_CSV = os.getenv("ACCOUNT_OVERVIEW_CSV")
ACCOUNT_OVERVIEW_JSON = os.getenv("ACCOUNT_OVERVIEW_JSON")
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_SCOPE = os.getenv("GOOGLE_SCOPE")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")