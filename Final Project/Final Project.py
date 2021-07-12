  
# This program gets data from a XML file from online 
# and display in requested way, it also check data validation.


import urllib.request

def get_information():
  cd_catalog = "https://www.w3schools.com/xml/cd_catalog.xml"
  return 


catalog_data = []
for line in cd_data.split("\n"):
    catalog_data.append(line)

print(catalog_data)

for invrement in range(0,len(catalog_data)-1,1):
    check = catalog_data[i].find("TITLE")
    if check >= 0:
        print(catalog_data[i])
