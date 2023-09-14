import match_expenditures
import csvToJson
import utils.googleService as googleService


def main():
    # Parse csv to match expenses with categories
    match_expenditures.traverse_csv_to_match_expenditures()

    # Authenticate and connect to google sheet
    googleService.connect_google_sheets()

    # Update the Google Sheets with the total expenses
    # worksheet.update("A1", "Total Expenses")
    # worksheet.update("B1", total_expenses)


if __name__ == "__main__":
    main()
