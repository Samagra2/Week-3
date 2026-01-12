import pandas as pd

df = pd.read_csv("sales_data.csv")

df.fillna(0, inplace=True)
df.drop_duplicates(inplace=True)

total_revenue = df["Total_Sales"].sum()
average_sales = df["Total_Sales"].mean()
highest_sale = df["Total_Sales"].max()
lowest_sale = df["Total_Sales"].min()

best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()
best_region = df.groupby("Region")["Total_Sales"].sum().idxmax()

print("SALES ANALYSIS REPORT")
print(f"Total Revenue: ₹{total_revenue}")
print(f"Average Sales: ₹{average_sales}")
print(f"Highest Sale: ₹{highest_sale}")
print(f"Lowest Sale: ₹{lowest_sale}")
print(f"Best Product: {best_product}")
print(f"Top Region: {best_region}")
