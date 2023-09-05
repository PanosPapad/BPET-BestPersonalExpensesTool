expense_categories = {
    "Housing Expenses": ["Rent"],
    "Food and Dining": ["Groceries", "Coffee"],
    "Transportation": ["Train", "Gas"],
}

filter_words = {
    "NS": ["Train"],
    "Starbucks": ["Coffee"],
    "Lidl": ["Groceries"],
    "Scamgency": ["Rent"]
}

# Create a mapping of categories to integer values initialized to 0
amounts_per_category = {category: 0 for subcategories in expense_categories.values() for category in subcategories}
