import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Load dataset

df = pd.read_csv(
    "dataset/Personal_Finance_Dataset.csv"
)

# Convert Date

df['Date'] = pd.to_datetime(df['Date'])

# Extract month

df['Month'] = df['Date'].dt.month

# Keep only expenses

expense_df = df[df['Type'] == 'Expense']

# Group monthly expenses

monthly_expense = expense_df.groupby(
    'Month'
)['Amount'].sum().reset_index()

# Features and target

X = monthly_expense[['Month']]

y = monthly_expense['Amount']

# Train model

model = LinearRegression()

model.fit(X, y)

# Save model

joblib.dump(
    model,
    "ml/expense_prediction_model.pkl"
)

print("Model Trained Successfully")