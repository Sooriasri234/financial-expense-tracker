import pandas as pd

# Load dataset
df = pd.read_csv("dataset/Personal_Finance_Dataset.csv")

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Check dataset
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nDataset Info:")
print(df.info())

print("\nNull Values:")
print(df.isnull().sum())

print("\nExpense Categories:")
print(df['Category'].unique())

print("\nTransaction Types:")
print(df['Type'].unique())