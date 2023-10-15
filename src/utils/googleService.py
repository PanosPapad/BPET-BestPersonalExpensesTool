import gspread
import oauth2client.client
import src.utils.appConfig as Env
import src.constants as Constants


def connect_google_sheets():
    # connect to the service account
    gc = gspread.service_account(filename=Env.GOOGLE_CLIENT_SERVICE_CREDS)

    # connect to the sheet
    sheet = gc.open("BPET-BestPersonalExpensesToolTEST").sheet1

    # Test step. Remove
    # sheet.update(Constants.data_in_sheet['categories'][0], 12)
