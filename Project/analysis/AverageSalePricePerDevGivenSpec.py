import pandas as pd
import matplotlib.pyplot as plt


salesDataset = pd.read_csv("C:/Users/khaml/Desktop/Real-Estate-Dubai-Data-Manipulation/data/Sales_ColumnsOfInterest.csv")

average_prices_per_development = salesDataset.groupby(['project_name_en', 'rooms_en'])['actual_worth'].mean().reset_index(name='average_prices_per_development')


print(average_prices_per_development)
average_prices_per_development.to_csv('AverageSalePricePerDevGivenSpec.csv', index=False)

