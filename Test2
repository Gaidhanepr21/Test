import pandas as pd

# Load data from Excel file
file_path = 'transactions_data.xlsx'
df = pd.read_excel(file_path)

# Display the DataFrame to verify data types and content
print("Original DataFrame:")
print(df)

# Assume the Excel file has a column 'transaction_type' that contains the type of transaction
# If necessary, convert the 'transaction_type' column to string type
df['transaction_type'] = df['transaction_type'].astype(str)

# Calculate the number of occurrences of each transaction type
transaction_counts = df['transaction_type'].value_counts()

# Print the number of occurrences of each transaction type
print("\nNumber of Occurrences of Each Transaction Type:")
print(transaction_counts)
