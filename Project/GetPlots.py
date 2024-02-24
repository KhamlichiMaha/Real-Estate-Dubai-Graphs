from matplotlib import pyplot as plt
from GetDataframes import GetDataframes

areas = [
    "Burj Khalifa",
    "Al Jadaf",
    "Al Barsha First",
    "Al Wasl",
    "Marsa Dubai",
    "Palm Jumeirah"
]
areaDataframes = {}

for i, area in enumerate(areas):
    areaDataframes[area] = GetDataframes(area)

plt.figure()
for i, area in enumerate(areas):
    sales = areaDataframes[area][0]
    plt.plot(sales['year'], sales['meter_sale_price_gbp'], label=area)
plt.xlabel('Year')
plt.ylabel('Average Meter Sale Price (GBP)')
plt.legend()
plt.savefig('SalesComparison.png')

plt.figure()
for i, area in enumerate(areas):
    sales = areaDataframes[area][1]
    plt.plot(sales['year'], sales['monthly_amount_per_square_meter_gbp'], label=area)
plt.xlabel('Year')
plt.ylabel('Average Monthly Rent Per Square Meter (GBP)')
plt.legend()
plt.savefig('RentComparison.png')

plt.figure()
for i, area in enumerate(areas):
    sales = areaDataframes[area][2]
    plt.plot(sales['year'], sales['PE_Ratio'], label=area)
plt.xlabel('Year')
plt.ylabel('PE Ratio')
plt.legend()
plt.savefig('PERatioComparison.png')

# Overlap in 'area_en' columns:
# Warsan Fourth
# Al Safouh Second
# Al Goze Fourth
# Wadi Al Safa 4
# Al Merkadh
# Hessyan First
# Saih Shuaib 2
# Zaabeel First
# Al Hebiah Sixth
# Al Hebiah Fifth
# Al Thanyah Third
# Business Bay
# Hadaeq Sheikh Mohammed Bin Rashid
# Al Qusais Industrial Fifth
# Al Kheeran
# Nadd Hessa
# Palm Jumeirah
# Al Thanyah Fifth
# Madinat Al Mataar
# Al Barsha First
# Jabal Ali First
# Rega Al Buteen
# Al Qusais Industrial Fourth
# Al Warsan First
# Al Kifaf
# Madinat Hind 4
# Marsa Dubai
# Al Barsha South Fifth
# Zaabeel Second
# Dubai Investment Park Second
# Um Hurair Second
# Wadi Al Safa 3
# Nad Al Shiba First
# Nad Al Hamar
# Madinat Dubai Almelaheyah
# Al Hebiah Fourth
# Al Hebiah Second
# Wadi Al Safa 2
# Wadi Al Safa 5
# Al Hebiah Third
# Trade Center Second
# Al Barshaa South Third
# Me'Aisem First
# Al Hebiah First
# Muhaisanah First
# Al Barshaa South Second
# Al Thanyah First
# Um Suqaim Third
# Al Khairan First
# Island 2
# Al Barsha South Fourth
# Burj Khalifa
# Al Safouh First
# Jumeirah First
# Al Wasl
# Mirdif
# Jabal Ali Industrial Second
# Dubai Investment Park First
# Al Jadaf
# Al Yelayiss 2