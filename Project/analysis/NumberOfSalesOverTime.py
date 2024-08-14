import pandas as pd
import matplotlib.pyplot as plt


salesDataset = pd.read_csv("C:/Users/khaml/Desktop/Real-Estate-Dubai-Data-Manipulation/data/Sales_ColumnsOfInterest.csv")
salesDataset['instance_date'] = pd.to_datetime(salesDataset['instance_date'], format='%d-%m-%Y', errors='coerce')



salesDataset['year_month'] = salesDataset['instance_date'].dt.to_period('M')

salesDataset = salesDataset[salesDataset['instance_date'] > "01-01-2000"]
salesDataset = salesDataset[salesDataset['instance_date'] < "08-01-2024"]

counts_per_month = salesDataset.groupby('year_month').size().reset_index(name='counts')


print(counts_per_month)
counts_per_month.to_csv('NumberOfSalesOverTime.csv', index=False)

