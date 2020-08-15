import requests
import pandas as pd

# Step1 Data Collection

url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_India'
req = requests.get(url, timeout=2)


data_list = pd.read_html(req.text)
target_df = data_list[6]

# Data Cleaning
# issue 1 - Column Names/Header
target_df.columns = ['States', 'Total Cases', 'Total Deaths', 
                      'Total Recoveries', 'Col 5', 'Col 6', 'Col 7', 'Col 8', 
                      'Col 9']
# issue 2 - Extra Columns
target_df = target_df[['States', 'Total Cases', 'Total Deaths',
                       'Total Recoveries']]
# issue 3 - Extra Rows
# target_df = target_df.drop([36, 37])

last_idx = target_df.index[-1]
target_df = target_df.drop([last_idx, last_idx-1])

print(target_df.dtypes)

# issue 4 - Special characters
target_df['Total Cases'] = target_df['Total Cases'].str.replace('\[.*\]','')
target_df['Total Deaths'] = target_df['Total Deaths'].str.replace('\[.*\]','')

target_df['Total Cases'] = target_df['Total Cases'].str.replace(',','')

# issue 5 - Data Type
target_df['Total Cases'] = pd.to_numeric(target_df['Total Cases'])
target_df['Total Deaths'] = pd.to_numeric(target_df['Total Deaths'])
target_df['Total Recoveries'] = pd.to_numeric(target_df['Total Recoveries'])
 
# issue 7 - Sort The Data
target_df = target_df.sort_values(by = 'Total Cases', ascending = False)


# Export The Data 
target_df.to_excel('covid_india.xlsx')
# target_df.to_csv('covid_india.csv')
 






