  
# This program gets data from a XML file from online 
# and display in requested way, it also check data validation.


import urllib.request

def get_information():
  cd_catalog = "https://www.w3schools.com/xml/cd_catalog.xml"
  return 


catalog_data = []
for line in cd_data.split("\n"):
    catalog_data.append(line)
   

title_data = []
artist_data= []
company_data = []
country_data = []
price_data = []
year_data = []


for invrement in range(0,len(catalog_data)-1,1):
    check = catalog_data[increment].find("TITLE")
    if check >= 0:
        title_data.append(catalog_data[increment])
        print(catalog_data[increment])

for increment in range(0,len(catalog_data)-1,1):
    check = catalog_data[increment].find("ARTIST")
    if check >= 0:
        artist_data.append(catalog_data[i])
        print(catalog_data[increment])

for increment in range(0,len(catalog_data)-1,1):
    check = catalog_data[increment].find("COMPANY")
    if check >= 0:
        company_data.append(catalog_data[increment])
        print(catalog_data[increment])


for increment in range(0,len(catalog_data)-1,1):
    check = catalog_data[increment].find("COUNTRY")
    if check >= 0:
        country_data.append(catalog_data[increment])
        print(catalog_data[increment])


for increment in range(0,len(catalog_data)-1,1):
    check = catalog_data[increment].find("PRICE")
    if check >= 0:
        price_data.append(catalog_data[increment])
        print(catalog_data[increment])

for increment in range(0,len(catalog_data)-1,1):
    check = catalog_data[increment].find("YEAR")
    if check >= 0:
        year_data.append(catalog_data[increment])
        print(catalog_data[increment])
