import pandas as pd


def GetDataframes(area):
    # SALES
    salesDataset = pd.read_csv("C:/Users/khaml/Desktop/RealEstateDubai/data/Sales_Filtered.csv")
    salesDatasetClean = (salesDataset.replace({'meter_sale_price_gbp': {'': pd.NA, 0: pd.NA, float('inf'): pd.NA}})
                         .dropna(subset=['meter_sale_price_gbp']))
    salesDatasetClean['instance_date'] = pd.to_datetime(salesDatasetClean['instance_date'], format='%d-%m-%Y')
    salesDatasetClean['year'] = salesDatasetClean['instance_date'].dt.year

    averageMeterSalePricePerYear = salesDatasetClean.groupby(['area_name_en', 'year'])['meter_sale_price_gbp'].mean()
    averageMeterSalePricePerYear = averageMeterSalePricePerYear.reset_index()
    sales_df = averageMeterSalePricePerYear[averageMeterSalePricePerYear['area_name_en'] == area]

    # RENT
    rentDataset = pd.read_csv("C:/Users/khaml/Desktop/RealEstateDubai/data/Rent_Filtered.csv")
    rentDatasetClean = (rentDataset.replace({'monthly_amount_per_square_meter_gbp': {'': pd.NA, 0: pd.NA, float('inf'): pd.NA}})
                        .dropna(subset=['monthly_amount_per_square_meter_gbp']))
    rentDatasetClean['contract_start_date'] = pd.to_datetime(rentDatasetClean['contract_start_date'], format='%d-%m-%Y')
    rentDatasetClean['year'] = rentDatasetClean['contract_start_date'].dt.year

    averageMonthlyRentPerSquareMeterPerYear = rentDatasetClean.groupby(['area_name_en', 'year'])['monthly_amount_per_square_meter_gbp'].mean()
    averageMonthlyRentPerSquareMeterPerYear = averageMonthlyRentPerSquareMeterPerYear.reset_index()
    rent_df = averageMonthlyRentPerSquareMeterPerYear[averageMonthlyRentPerSquareMeterPerYear['area_name_en'] == area]

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

    return sales_df, rent_df, peRatio_df
