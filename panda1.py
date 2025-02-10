import pandas as pd
file_for_data = pd.read_csv("data.csv")
total_revenue = file_for_data.groupby('Product')['Revenue'].sum()
print(total_revenue)