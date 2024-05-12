import csv

# What is the number of total vaccinations done on 1/6/2021 (MM/DD/YYYY) by considering missing values imputed version of dataset?

total_vaccinations = 0

with open('new_country_vaccination_stats.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        if row['date'] == '1/6/2021':
            total_vaccinations += int(row['daily_vaccinations'])

print(total_vaccinations)
