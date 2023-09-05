import constants
import utils.appConfig as Env
import json


def find_matching_category(input_string):
    matching_categories = []
    for keyword, categories in constants.filter_words.items():
        if keyword.lower() in input_string.lower():
            matching_categories.extend(categories)
    return matching_categories


def traverse_json_to_match_expenditures():
    with open(Env.ACCOUNT_OVERVIEW_JSON, 'r') as jsonf:
        # Load the JSON data into a Python object
        data = json.load(jsonf)

    # Iterate through the JSON data and check for matches
    for item in data:
        name_description = item.get("Name / Description", "").strip()
        amount_eur = item.get("Amount (EUR)", "").replace(',', '.')
        debit_credit = item.get("Debit/credit", "")
        date = item.get("Date", "")

        if debit_credit == "Credit":
            continue

        if name_description:
            matched_categories = find_matching_category(name_description)
            if matched_categories:
                matched_category = matched_categories[0]  # It will always match one element
                process_expenditures(matched_category, amount_eur)
            else:
                print(f"No matches found for '{name_description}'")
        else:
            print("No 'Name / Description' field found in the JSON item.")


def process_expenditures(matched_category, amount_eur):
    constants.amounts_per_category[matched_category] += float(amount_eur.replace(',', '.'))
