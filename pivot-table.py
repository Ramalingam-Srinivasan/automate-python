import pandas as pd

# Load the Excel file into a DataFrame using openpyxl as the engine
df = pd.read_excel('requirement/Superstore.xlsx', engine='openpyxl')

# Select specific columns from the DataFrame
df = df[['Row ID', 'Discount', 'Profit']]

# Create a pivot table, summing the 'Profit' values, indexed by 'Row ID' and grouped by 'Discount'
pivot_table = df.pivot_table(index='Row ID', columns='Discount', values='Profit', aggfunc='sum').round(0)

# Optionally, print the pivot table for verification
# print(pivot_table)

# Export the pivot table to an Excel file, saving it in the 'report' sheet starting from row 0
pivot_table.to_excel('requirement/pivot_table.xlsx', 'report', startrow=0)
