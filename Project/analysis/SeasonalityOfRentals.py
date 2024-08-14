import pandas as pd
import matplotlib.pyplot as plt


rentalsDataset = pd.read_csv("C:/Users/khaml/Desktop/Real-Estate-Dubai-Data-Manipulation/data/Rent_ColumnsOfInterest.csv")
rentalsDataset['contract_start_date'] = pd.to_datetime(rentalsDataset['contract_start_date'], format='%d-%m-%Y', errors='coerce')

rentalsDataset['year_month'] = rentalsDataset['contract_start_date'].dt.to_period('M')

rentalsDataset = rentalsDataset[rentalsDataset['contract_start_date'] > "01-01-2000"]
rentalsDataset = rentalsDataset[rentalsDataset['contract_start_date'] < "08-01-2024"]

rentalsDataset['day'] = rentalsDataset['contract_start_date'].dt.day
rentalsDataset['month'] = rentalsDataset['contract_start_date'].dt.month
rentalsDataset['year'] = rentalsDataset['contract_start_date'].dt.year
rentalsDataset = rentalsDataset[~((rentalsDataset['day'] == 1) & (rentalsDataset['month'] == 1))]

counts_per_month_year = rentalsDataset.groupby(['year', 'month']).size().reset_index(name='counts')
average_rows_per_month = counts_per_month_year.groupby('month')['counts'].mean().reset_index(name='average_counts')

print(average_rows_per_month)
average_rows_per_month.to_csv('SeasonalityOfRentals.csv', index=False)

