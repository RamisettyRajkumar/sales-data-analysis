import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (Replace 'sales_data.csv' with your actual file path)
df = pd.read_csv('sales_data.csv')

# Display basic dataset info
print("Dataset Head:")
print(df.head())
print("\nSummary Statistics:")
print(df.describe())

# Total revenue analysis
df['Total_Sales'] = df['Quantity'] * df['Unit_Price']
total_revenue = df['Total_Sales'].sum()
print(f"\nTotal Revenue: ${total_revenue:,.2f}")

# Top-selling products
top_products = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False).head(10)
print("\nTop-Selling Products:")
print(top_products)

# Sales trend over time
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
daily_sales = df.groupby('Order_Date')['Total_Sales'].sum()

plt.figure(figsize=(12, 6))
sns.lineplot(x=daily_sales.index, y=daily_sales.values)
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

# Regional sales performance
region_sales = df.groupby('Region')['Total_Sales'].sum()
plt.figure(figsize=(8, 5))
sns.barplot(x=region_sales.index, y=region_sales.values, palette='coolwarm')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()

print("\nSales Data Analysis Completed!")
