from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

app = Flask(__name__)

# Dummy business performance data
data = {
    'business_id': [1, 2, 3],
    'name': ['Business A', 'Business B', 'Business C'],
    'revenue': [100000, 150000, 120000],
    'expenses': [70000, 90000, 80000],
    'growth_rate': [0.05, 0.10, 0.07]
}

df = pd.DataFrame(data)

def predict_future_performance(df):
    X = df[['revenue', 'expenses', 'growth_rate']]
    y = df['growth_rate']

    model = LinearRegression()
    model.fit(X, y)

    future_growth = model.predict(X)
    df['future_growth'] = future_growth

    return df

@app.route('/analyze', methods=['GET'])
def analyze():
    analyzed_data = predict_future_performance(df)
    result = analyzed_data.to_dict(orient='records')
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
  
