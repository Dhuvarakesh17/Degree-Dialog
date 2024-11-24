import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'sales_data.csv'  # Replace with your dataset file path
try:
    df = pd.read_csv(file_path)
    print("Data Loaded Successfully!")
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")

# Initial Data Overview
print("First 5 rows of the dataset:")
print(df.head())

print("\nBasic Information:")
print(df.info())

print("\nDescriptive Statistics:")
print(df.describe())

# Data Cleaning
# Handle missing values
print("\nNumber of missing values in each column:")
print(df.isnull().sum())

# Drop rows/columns with excessive missing data or fill missing values
df = df.dropna(subset=['Sales'])  # Example: Drop rows where 'Sales' is NaN
df['Customer Name'].fillna('Unknown', inplace=True)  # Example: Fill NaN in 'Customer Name'

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert columns to appropriate data types
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Convert 'Date' to datetime format
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')  # Ensure 'Sales' is numeric

# Exploratory Data Analysis (EDA)
# Sales trends over time
plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Sales', data=df)
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# Top products by sales
top_products = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products by Total Sales:")
print(top_products)

plt.figure(figsize=(10, 5))
top_products.plot(kind='bar')
plt.title('Top 10 Products by Sales')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()

# Sales distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['Sales'], bins=30, kde=True)
plt.title('Sales Distribution')
plt.xlabel('Sales')
plt.show()

# Correlation analysis
correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Save cleaned data
df.to_csv('cleaned_sales_data.csv', index=False)
print("\nCleaned data saved as 'cleaned_sales_data.csv'.")

print("Data cleaning and analysis complete.")
