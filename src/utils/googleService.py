import gspread
import oauth2client.client
import appConfig as Env


def connect_google_sheets():
    # connect to the service account
    gc = gspread.service_account(filename=Env.GOOGLE_CLIENT_SERVICE_CREDS)

    # connect to the sheet
    sheet = gc.open("BPET-BestPersonalExpensesToolTEST").sheet1
