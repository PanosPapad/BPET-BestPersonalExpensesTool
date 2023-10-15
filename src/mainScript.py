import match_expenditures
import csvToJson
import utils.googleService as googleService
import csv
import constants


def main():
    # Parse csv to match expenses with categories
    match_expenditures.traverse_csv_to_match_expenditures()

    # Authenticate and connect to google sheet
    googleService.connect_google_sheets()

    #Temporary output of amounts of all categories in a single csv to pass to the spreadsheet
    data = [{'Category': category, 'Amount': amount} for category, amount in constants.amounts_per_category.items()]

    with open('../files/rawAmountOutput.csv', 'w', newline='') as csvfile:
        fieldnames = ['Category', 'Amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)

    # Update the Google Sheets with the total expenses
    # sheet.update(constants.data_in_sheet['categories'][0], 12)



if __name__ == "__main__":
    main()
