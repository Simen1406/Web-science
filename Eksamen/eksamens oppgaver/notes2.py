import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index"
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

# Get the first table in the page
table = soup.find_all('table', {'class': 'wikitable'})[1]

# Loop through each row in the table
for row in table.find_all('tr')[1:]:  # Exclude header row
    columns = row.find_all('td')

    # Ensure that the row has at least 3 columns (Rank, Country/Territory, and HDI)
    if len(columns) >= 3:
        country_column = columns[1]
        hdi_column = columns[2]

        # Check if there's an 'a' tag in the country column, otherwise get the text directly
        country_tag = country_column.find('a')
        if country_tag:
            country = country_tag.text.strip()
        else:
            country = country_column.text.strip()

        hdi = hdi_column.text.strip()

        print(f"{country} - {hdi}")