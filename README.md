# Country Vaccination Statistics Imputation

This repository contains solutions to various tasks related to imputing missing daily vaccination numbers in a dataset of country vaccination statistics.

## Files

- `country_vaccination_stats.csv`: The original dataset containing daily vaccination numbers.
- `new_country_vaccination_stats.csv`: The dataset with imputed daily vaccination numbers.
- `impute_min.py`: Python script to impute missing values with the minimum daily vaccination numbers per country.
- `top_3_median_vaccinations.py`: Python script to list the top-3 countries with the highest median daily vaccination numbers.
- `total_vaccinations_2021_01_06.py`: Python script to calculate the total number of vaccinations done on January 6, 2021.
- `impute_median.sql`: SQL script to impute missing values with the median daily vaccination numbers per country.

# Questions and Solutions

## Question 4: Impute Missing Daily Vaccination Numbers with Minimum Values

**Task**: Implement code to fill the missing data in the `daily_vaccinations` column per country with the minimum daily vaccination number of relevant countries. If a country does not have any valid vaccination numbers yet, fill it with "0".

**Solution**: This task is addressed by the `impute_min.py` script.

### `impute_min.py`
import csv

### Step 1: Calculate the minimum daily vaccination number for each country
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

### Step 2: Impute missing daily vaccination numbers with the minimum value found for that country
with open('country_vaccination_stats.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)

    header = rows[0]  # Save the header
    for i, row in enumerate(rows[1:], start=1):
        country = row[0]
        daily_vaccinations = row[2]
        
        if not daily_vaccinations.strip():  # Check if the daily_vaccinations field is empty
            min_value = min_vaccinations.get(country, 0)  # Get the minimum value or default to 0
            rows[i][2] = str(min_value)

### Step 3: Save the updated data back to a new CSV file
with open('new_country_vaccination_stats.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header)  # Write the header first
    csv_writer.writerows(rows[1:])  # Write the data rows

print("Imputation complete. Results saved to 'new_country_vaccination_stats.csv'.")


## Question 6: List Top 3 Countries with the Highest Median Daily Vaccination Numbers

**Task:** Implement code to list the top 3 countries with the highest median daily vaccination numbers by considering the dataset with imputed values.

**Solution:** This task is addressed by the following code snippet.

import csv

from statistics import median

**Script to find top-3 countries with highest median daily vaccination numbers**

...

**Usage**

python top_3_median_vaccinations.py


## Question 8: SQL Query to Impute Missing Values with Median Values

**Task:** Provide an SQL query to fill in the missing daily vaccination numbers with the median of each country. If a country does not have any valid daily vaccination records, fill it with "0".

**Solution:** This task is addressed by the impute_median.sql script.


### `SQL script to impute missing values with median daily vaccination numbers;`

CREATE TEMPORARY TABLE temp_medians AS

SELECT country, PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY daily_vaccinations) AS country_median
FROM country_vaccination_stats

WHERE daily_vaccinations IS NOT NULL

GROUP BY country;

--------------------

UPDATE country_vaccination_stats AS t1

SET daily_vaccinations = t2.country_median

FROM temp_medians AS t2

WHERE t1.country = t2.country

AND (t1.daily_vaccinations IS NULL OR t1.daily_vaccinations = '');

--------------------

UPDATE country_vaccination_stats

SET daily_vaccinations = 0

WHERE daily_vaccinations IS NULL OR daily_vaccinations = '';

## Question 7: Calculate Total Vaccinations on 2021-01-06

**Task:** Calculate the number of total vaccinations done on January 6, 2021 (MM/DD/YYYY) by considering the dataset with imputed values.

**Solution:** This task is addressed by the total_vaccinations_2021_01_06.py script.


`total_vaccinations_2021_01_06.py`

import csv

**Initialize the total vaccinations counter**

total_vaccinations = 0

**Open and read the imputed dataset**

with open('new_country_vaccination_stats.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Iterate through each row in the dataset
    for row in csv_reader:
        # Check if the date matches '1/6/2021'
        if row['date'] == '1/6/2021':
            # Add the daily vaccinations to the total
            total_vaccinations += int(row['daily_vaccinations'])

**Print the total number of vaccinations done on 1/6/2021**

print(total_vaccinations)
