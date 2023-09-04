import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access environment variables and assign them as global variables


ACCOUNT_OVERVIEW_CSV = os.getenv("ACCOUNT_OVERVIEW_CSV")
ACCOUNT_OVERVIEW_JSON = os.getenv("ACCOUNT_OVERVIEW_JSON")
