import csv
from statistics import median

# Question 6
# Code Implementation Task: Implement code to list the top-3 countries with highest median daily vaccination numbers by considering missing values imputed version of dataset.

data = []

with open('new_country_vaccination_stats.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        data.append(row)

# 1- We are calculating the median daily vaccination numbers for each country.
country_medians = {}

for row in data:
    country = row['country']
    daily_vaccinations = int(row['daily_vaccinations'])
    
    if country not in country_medians:
        country_medians[country] = [daily_vaccinations]
    else:
        country_medians[country].append(daily_vaccinations)

# 2- We sort the countries based on their median daily vaccination numbers.
sorted_countries = sorted(country_medians.items(), key=lambda x: median(x[1]), reverse=True)

# 3- Finally, we print the top 3 countries with the highest median daily vaccination numbers.
print("Top 3 countries with highest median daily vaccination numbers:")
for i, (country, medians) in enumerate(sorted_countries[:3]):
    print(f"{i+1}. {country}: {median(medians)}")




