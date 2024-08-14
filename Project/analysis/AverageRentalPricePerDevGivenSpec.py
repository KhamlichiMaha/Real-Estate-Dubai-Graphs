import pandas as pd
import matplotlib.pyplot as plt


rentalsDataset = pd.read_csv("C:/Users/khaml/Desktop/Real-Estate-Dubai-Data-Manipulation/data/Rent_ColumnsOfInterest.csv")

average_prices_per_development = rentalsDataset.groupby(['project_name_en', 'ejari_property_sub_type_en'])['annual_amount'].mean().reset_index(name='average_prices_per_development')


print(average_prices_per_development)
average_prices_per_development.to_csv('AverageRentalPricePerDevGivenSpec.csv', index=False)

