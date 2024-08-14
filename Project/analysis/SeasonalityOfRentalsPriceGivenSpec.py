import pandas as pd
import matplotlib.pyplot as plt


rentalsDataset = pd.read_csv("C:/Users/khaml/Desktop/Real-Estate-Dubai-Data-Manipulation/data/Rent_ColumnsOfInterest.csv")
rentalsDataset['contract_start_date'] = pd.to_datetime(rentalsDataset['contract_start_date'], format='%d-%m-%Y', errors='coerce')

rentalsDataset['year_month'] = rentalsDataset['contract_start_date'].dt.to_period('M')

rentalsDataset = rentalsDataset[rentalsDataset['contract_start_date'] > "01-01-2000"]
rentalsDataset = rentalsDataset[rentalsDataset['contract_start_date'] < "08-01-2024"]

rentalsDataset['month'] = rentalsDataset['contract_start_date'].dt.month
rentalsDataset['year'] = rentalsDataset['contract_start_date'].dt.year

average_worth_per_month_rooms = rentalsDataset.groupby(['month', 'ejari_property_sub_type_en'])['annual_amount'].mean().reset_index(name='average_actual_worth')


print(average_worth_per_month_rooms)
average_worth_per_month_rooms.to_csv('SeasonalityOfRentalsPriceGivenSpec.csv', index=False)

