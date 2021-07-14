  
# This program gets data from a XML file from online 
# and display in requested way, it also check data validation.


import urllib.request

def get_information():
  cd_catalog = "https://www.w3schools.com/xml/cd_catalog.xml"
  try:
        cd_data = urllib.request.urlopen(cd_catalog).read().decode()
        main_data = cd_data.split("<TITLE>")
  except Exception as exception:
        print("Try to connect internet or web page not available")
        exit(1)
    return main_data

def get_title_array(record):
    get_record = record.split("\n")
    data = ""
    for i in range(0,len(get_record),1):
        if(get_record[i].find("TITLE") > 0):
            end  = get_record[i].find("</TITLE>")
            data = get_record[i][:end]
    return data



def get_data_array(main_data):
    title_data = []
    for i in range(1,len(main_data)-1,1):
        title_data.append(get_title_array(main_data[i]))

    print(title_data)
  
  
'''catalog_data = []
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
        print(catalog_data[increment])'''

        
def main():
    main_data = fetch_info()
    print(main_data)



main()
