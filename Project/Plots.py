import pandas as pd
import matplotlib.pyplot as plt

# Input Area
area = "Jabal Ali Industrial Second"

# SALES
salesDataset = pd.read_csv("C:/Users/khaml/Desktop/RealEstateDubai/data/Sales_Filtered.csv")
salesDatasetClean = (salesDataset.replace({'meter_sale_price_gbp': {'': pd.NA, 0: pd.NA, float('inf'): pd.NA}})
                    .dropna(subset=['meter_sale_price_gbp']))
salesDatasetClean['instance_date'] = pd.to_datetime(salesDatasetClean['instance_date'], format='%d-%m-%Y')
salesDatasetClean['year'] = salesDatasetClean['instance_date'].dt.year

averageMeterSalePricePerYear = salesDatasetClean.groupby(['area_name_en', 'year'])['meter_sale_price_gbp'].mean()
averageMeterSalePricePerYear = averageMeterSalePricePerYear.reset_index()
sales_df = averageMeterSalePricePerYear[averageMeterSalePricePerYear['area_name_en'] == area]

plt.figure()
salesPlot = plt.plot(sales_df['year'], sales_df['meter_sale_price_gbp'], label=area)
plt.xlabel('Year')
plt.ylabel('Average Meter Sale Price (GBP)')
plt.legend()
plt.savefig('AverageSquareMeterPrice_vs_Time.png')


# RENT
rentDataset = pd.read_csv("C:/Users/khaml/Desktop/RealEstateDubai/data/Rent_Filtered.csv")
rentDatasetClean = (rentDataset.replace({'monthly_amount_per_square_meter_gbp': {'': pd.NA, 0: pd.NA, float('inf'): pd.NA}})
                    .dropna(subset=['monthly_amount_per_square_meter_gbp']))
rentDatasetClean['contract_start_date'] = pd.to_datetime(rentDatasetClean['contract_start_date'], format='%d-%m-%Y')
rentDatasetClean['year'] = rentDatasetClean['contract_start_date'].dt.year

averageMonthlyRentPerSquareMeterPerYear = rentDatasetClean.groupby(['area_name_en', 'year'])['monthly_amount_per_square_meter_gbp'].mean()
averageMonthlyRentPerSquareMeterPerYear = averageMonthlyRentPerSquareMeterPerYear.reset_index()
rent_df = averageMonthlyRentPerSquareMeterPerYear[averageMonthlyRentPerSquareMeterPerYear['area_name_en'] == area]

plt.figure()
rentPlot = plt.plot(rent_df['year'], rent_df['monthly_amount_per_square_meter_gbp'], label=area)
plt.xlabel('Year')
plt.ylabel('Average Monthly Rent Per Square Meter (GBP)')
plt.legend()
plt.savefig('AverageMonthlyRentPerSquareMeter_vs_Time.png')

#Overlap in area values from both CSVs
sales_areas = set(salesDatasetClean['area_name_en'].unique())
rent_areas = set(rentDatasetClean['area_name_en'].unique())

overlap_areas = sales_areas.intersection(rent_areas)
overlap_years = set(sales_df['year']).intersection(rent_df['year'])

sales_filteredYears_df = sales_df[sales_df['year'].isin(overlap_years)]
rent_filteredYears_df = rent_df[rent_df['year'].isin(overlap_years)]

years = []
peRatio = []

for year in sorted(overlap_years):
    years.append(year)
    salePrice = sales_filteredYears_df[sales_filteredYears_df['year'] == year]['meter_sale_price_gbp'].iloc[0]
    rentPrice = rent_filteredYears_df[rent_filteredYears_df['year'] == year]['monthly_amount_per_square_meter_gbp'].iloc[0]

    peRatio.append(salePrice/rentPrice)

peRatio_df = pd.DataFrame({'year': years, 'PE_Ratio': peRatio})

print("Overlap in 'area_en' columns:")
for a in overlap_areas:
    print(a)

#PRICE TO EARNING RATIO
plt.figure()
PEPlot = plt.plot(peRatio_df['year'], peRatio_df['PE_Ratio'], label=area)
plt.xlabel('Year')
plt.ylabel('PE Ratio')
plt.legend()
plt.savefig('PE_Ratio.png')


# TODO
# Calculate the average PE ratio across areas over time
# For each year compute the average of the available areas for that year. No need for the intersection
# So we get the overall PE ratio for Dubai

# See many lines on the same graph: Créer un nouveau fichier, met tout ce que j'ai fait dans une fonction that
# outputs 3 dataframes and takes in a single area
# Example: def getData(areaName)

# Then create another function that calls the first one many times