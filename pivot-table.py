import pandas as pd

df = pd.read_excel('requirement/Superstore.xlsx',engine='openpyxl')
df=df[['Row ID','Discount','Profit']]
pivot_table= df.pivot_table(index='Row ID',columns='Discount',values='Profit',aggfunc='sum').round(0)
#print(pivot_table)
pivot_table.to_excel('requirement/pivot_table.xlsx','report',startrow=0)