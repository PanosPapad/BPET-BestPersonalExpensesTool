import csv
import json
import utils.appConfig as Env

# Initialize an empty list to store the data
data = []


def convert_bank_statement():
    # Open and read the CSV file
    with open(Env.ACCOUNT_OVERVIEW_CSV, 'r') as csvf:
        # Create a CSV reader object
        csv_reader = csv.DictReader(csvf)

        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Append each row (represented as a dictionary) to the data list
            data.append(row)

    # Open and write the JSON file
    with open(Env.ACCOUNT_OVERVIEW_JSON, 'w') as jsonf:
        # Write the data list to the JSON file
        json.dump(data, jsonf, indent=4)
