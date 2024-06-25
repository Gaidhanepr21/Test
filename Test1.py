import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np

# Load data from Excel file
file_path = 'business_data.xlsx'
df = pd.read_excel(file_path)

# Display the DataFrame to verify data types and content
print("Original DataFrame:")
print(df)

# Ensure text values in the 'name' column are read correctly
df['name'] = df['name'].astype(str)  # Explicitly converting to string if necessary

# Clean the data by ensuring numeric columns are correctly formatted
numeric_columns = ['revenue', 'expenses', 'growth_rate']

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert columns to numeric, set errors to NaN

# Drop rows with NaN values in essential columns
df.dropna(subset=numeric_columns, inplace=True)

# Separate features and target variable
X = df[['name', 'revenue', 'expenses']]
y = df['growth_rate']

# Create a ColumnTransformer to apply OneHotEncoder to the 'name' column
preprocessor = ColumnTransformer(
    transformers=[
        ('name', OneHotEncoder(), ['name']),
        ('revenue', 'passthrough', ['revenue']),
        ('expenses', 'passthrough', ['expenses'])
    ]
)

# Create a pipeline that includes the preprocessor and the linear regression model
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', LinearRegression())
])

# Train the model
pipeline.fit(X, y)

# Predict future growth rates
df['predicted_growth_rate'] = pipeline.predict(X)

# Suggest the best business for the future based on predicted growth rate
best_business = df.loc[df['predicted_growth_rate'].idxmax()]

# Output the results
print("\nAnalysis of Business Growth:")
print(df)
print("\nBest Business for the Future:")
print(best_business[['business_id', 'name', 'predicted_growth_rate']])
