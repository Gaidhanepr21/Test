import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Step 1: Read JSON data from file
def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Step 2: Parse JSON and extract relevant fields
def parse_json_data(json_data):
    payments = json_data['data']['payments']
    transactions = []
    for payment in payments:
        transaction = {
            'reference': payment['reference'],
            'currency': payment['currency'],
            'amount': payment['amount']
        }
        transactions.append(transaction)
    return transactions

# Step 3: Categorize transactions based on 'reference'
def categorize_transactions(transactions):
    categories = {}
    for transaction in transactions:
        reference = transaction['reference']
        if reference not in categories:
            categories[reference] = {
                'total_transactions': 0,
                'total_amount': 0.0,
                'average_amount': 0.0
            }
        categories[reference]['total_transactions'] += 1
        categories[reference]['total_amount'] += transaction['amount']
    
    # Calculate average amount for each category
    for category in categories:
        categories[category]['average_amount'] = categories[category]['total_amount'] / categories[category]['total_transactions']
    
    return categories

# Step 4: Machine Learning - Predicting which category is performing well
def predict_performance(categories):
    # Prepare data for ML model
    data = pd.DataFrame.from_dict(categories, orient='index')
    data.reset_index(inplace=True)
    data.rename(columns={'index': 'reference'}, inplace=True)
    
    # Feature engineering: Use total_transactions, total_amount, and average_amount as features
    X = data[['total_transactions', 'total_amount', 'average_amount']]
    y = data['reference']  # Category (reference) as target
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train a Random Forest classifier
    clf = RandomForestClassifier(random_state=42)
    clf.fit(X_train, y_train)
    
    # Evaluate the classifier
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))
    
    # Feature importance
    feature_importance = dict(zip(X.columns, clf.feature_importances_))
    print("Feature Importance:", feature_importance)
    
    # Predicting categories based on trained model
    future_categories = clf.predict(X)
    return future_categories

# Example usage:
if __name__ == '__main__':
    # Assuming your JSON data is stored in a file named 'transactions.json'
    filename = 'transactions.json'
    json_data = read_json_file(filename)
    transactions = parse_json_data(json_data)
    categories = categorize_transactions(transactions)
    print("Categories:", categories)
    
    predicted_future_categories = predict_performance(categories)
    print("Predicted Future Categories:", predicted_future_categories)
