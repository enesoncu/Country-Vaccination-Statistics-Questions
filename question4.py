import csv

# Question 4:
# Code Implementation Task: Implement code to fill the missing data (impute) in daily_vaccinations column per country with the minimum daily vaccination number of relevant countries.  
# Note: If a country does not have any valid vaccination number yet, fill it with “0” (zero). 


# Minimum daily vaccination number for each country.
min_vaccinations = {}

with open('country_vaccination_stats.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        country = row['country']
        daily_vaccinations = row['daily_vaccinations']
        
        if daily_vaccinations.isdigit():
            daily_vaccinations = int(daily_vaccinations)
            if country not in min_vaccinations or daily_vaccinations < min_vaccinations[country]:
                min_vaccinations[country] = daily_vaccinations

# Missing daily vaccination numbers with the minimum value found for that country.
print("Imputing missing data...")
with open('country_vaccination_stats.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)

    for i, row in enumerate(rows):
        country = row[0]
        daily_vaccinations = row[2]
        
        if not daily_vaccinations.strip():  
            min_value = min_vaccinations.get(country, 0) 
            rows[i][2] = str(min_value)
            print(f"Imputed missing data for {country}: {min_value}")

# Updated data back to the a new CSV file.
with open('new_country_vaccination_stats.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(rows)

print("Imputation complete. Results saved to 'country_vaccination_stats_imputed.csv'.")

# We find the minimum number of daily vaccinations for each country.
# We fill in the empty daily vaccination numbers with the minimum value we found for the relevant country.
