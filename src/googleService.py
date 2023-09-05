import gspread
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run_flow
from oauth2client.file import Storage
import utils.appConfig as Env

# Set up OAuth 2.0 flow
flow = OAuth2WebServerFlow(Env.GOOGLE_CLIENT_ID, Env.GOOGLE_CLIENT_SECRET, Env.GOOGLE_SCOPE, Env.GOOGLE_REDIRECT_URI)

# Run the flow to obtain credentials
storage = Storage('key.json')  # You can choose the storage location
credentials = run_flow(flow, storage)

# Authorize with Google Sheets API
gc = gspread.authorize(credentials)

sh = gc.open("BPET-BestPersonalExpensesTool").sheet1
