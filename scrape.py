#Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json 

class TableScraper:
    def __init__(self, name, url, container_indentification, identification_type="id", container = "table"):
        self.name = name    # instance variable unique to each instance
        self.url = url
        self.container_indentification = container_indentification
        self.identification_type = identification_type
        self.container = container
    
    def get(format = "csv"):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, 'lxml')

        if self.identification_type == "class":
            table = soup.find(self.container, class_=self.container_indentification)
def scrape_table( name, url, container_indentification, identification_type="id", container = "table", format="csv"):
# Create an URL object
# url = 'https://www.worldometers.info/coronavirus/'# Create object page
url ="https://finance.yahoo.com/trending-tickers/"
page = requests.get(url)

#https://finance.yahoo.com/trending-tickers/

# parser-lxml = Change html to Python friendly format
# Obtain page's information
soup = BeautifulSoup(page.text, 'lxml')
# soup

# Obtain information from tag <table>
table1 = soup.find("table", class_="W(100%)")
# table1

# Obtain every title of columns with tag <th>
headers = []
for i in table1.find_all('th'):
 title = i.text
 headers.append(title)

 # Convert wrapped text in column 13 into one line text
# headers[13] = 'Tests/1M pop'      

# Create a dataframe
mydata = pd.DataFrame(columns = headers)


# Create a for loop to fill mydata
for j in table1.find_all('tr')[1:]:
 row_data = j.find_all('td')
 row = [i.text for i in row_data]
 length = len(mydata)
 mydata.loc[length] = row

 print(mydata)

 mydata.to_csv("stocks.csv", index=False)