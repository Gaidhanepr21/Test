import json

# Function to categorize payments based on status
def categorize_by_status(payments):
    status_categories = {}
    for payment in payments:
        status = payment['status']
        if status not in status_categories:
            status_categories[status] = []
        status_categories[status].append(payment)
    return status_categories

# Function to categorize payments based on amount
def categorize_by_amount(payments, threshold=10.0):
    high_value = []
    low_value = []
    for payment in payments:
        amount = payment['amount']
        if amount > threshold:
            high_value.append(payment)
        else:
            low_value.append(payment)
    return {"high_value": high_value, "low_value": low_value}

# Function to categorize payments based on currency
def categorize_by_currency(payments):
    currency_categories = {}
    for payment in payments:
        currency = payment['currency']
        if currency not in currency_categories:
            currency_categories[currency] = []
        currency_categories[currency].append(payment)
    return currency_categories

# Function to read JSON data from a file
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to predict the next status of payments (dummy prediction)
def predict_next_status(current_status):
    # Simple dummy prediction logic for illustration
    if current_status == "COMPLETED":
        return "SETTLED"
    elif current_status == "PENDING":
        return "COMPLETED"
    else:
        return "PENDING"

# Main function
def main():
    file_path = 'payments.json'  # Update with your JSON file path
    data = read_json_file(file_path)
    
    payments = data['data']['payments']
    
    # Categorize by status
    status_categories = categorize_by_status(payments)
    print("Categorized by Status:")
    print(status_categories)
    
    # Categorize by amount
    amount_categories = categorize_by_amount(payments)
    print("Categorized by Amount:")
    print(amount_categories)
    
    # Categorize by currency
    currency_categories = categorize_by_currency(payments)
    print("Categorized by Currency:")
    print(currency_categories)
    
    # Predict next status for each payment
    predictions = {payment['id']: predict_next_status(payment['status']) for payment in payments}
    print("Predictions for Next Status:")
    print(predictions)

if __name__ == "__main__":
    main()
