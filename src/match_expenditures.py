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
        if name_description:
            matched_categories = find_matching_category(name_description)
            if matched_categories:
                print(f"Matched Categories for '{name_description}': {', '.join(matched_categories)}")
            else:
                print(f"No matches found for '{name_description}'")
        else:
            print("No 'Name / Description' field found in the JSON item.")
            