  
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
    data = "Not Available"
    for increment in range(0,len(get_record),1):
        if(get_record[increment].find("TITLE") > 0):
            end  = get_record[increment].find("</TITLE>")
            data = get_record[increment][:end]
    return data

def get_data_title(main_data):
    title_data = []
    for increment in range(1,len(main_data),1):
        title_data.append(get_title_array(main_data[increment]))
    return title_data
  
def get_artist_array(record):
    get_record = record.split("\n")
    data = "Not Available"
    for increment in range(0,len(get_record),1):
        if(get_record[increment].find("ARTIST") > 0):
            start = get_record[increment].find(">") + 1
            end  = get_record[increment].find("</ARTIST>")
            data = get_record[increment][start:end]
    return data

def get_data_artist(main_data):
    artist_data = []
    for increment in range(1,len(main_data),1):
        artist_data.append(get_artist_array(main_data[increment]))
    return artist_data


def get_country_array(record):
    get_record = record.split("\n")
    data = "Not Available"
    for increment in range(0,len(get_record),1):
        if(get_record[increment].find("COUNTRY") > 0):
            start = get_record[increment].find(">") + 1
            end  = get_record[increment].find("</COUNTRY>")
            data = get_record[increment][start:end]
    return data

def get_data_country(main_data):
    country_data = []
    for increment in range(1,len(main_data),1):
        country_data.append(get_country_array(main_data[increment]))
    print(country_data)
    return country_data

def get_company_array(record):
    get_record = record.split("\n")
    data = "Not Available"
    for increment in range(0,len(get_record),1):
        if(get_record[increment].find("COMPANY") > 0):
            start = get_record[increment].find(">") + 1
            end  = get_record[increment].find("</COMPANY>")
            data = get_record[increment][start:end]
    return data

def get_data_company(main_data):
    company_data = []
    for increment in range(1,len(main_data),1):
        company_data.append(get_company_array(main_data[increment]))
    return company_data

def get_price_array(record):
    get_record = record.split("\n")
    data = "0.00"
    for increment in range(0,len(get_record),1):
        if(get_record[increment].find("PRICE") > 0):
            start = get_record[increment].find(">") + 1
            end  = get_record[increment].find("</PRICE>")
            data = get_record[increment][start:end]
    return data

def get_data_price(main_data):
    price_data = []
    for increment in range(1,len(main_data),1):
        price_data.append(get_price_array(main_data[increment]))
    return price_data


def get_year_array(record):
    get_record = record.split("\n")
    data = "Not Available"
    for i in range(0,len(get_record),1):
        if(get_record[increment].find("YEAR") > 0):
            start = get_record[increment].find(">") + 1
            end  = get_record[increment].find("</YEAR>")
            data = get_record[increment][start:end]
    return data

def get_data_year(main_data):
    year_data = []
    for increment in range(1,len(main_data),1):
        year_data.append(get_year_array(main_data[i]))
    return year_data
  
def display_output(title_data,artist_data,country_data,company_data,price_data,year_data):
    for i in range (0, len(title_data),1):
        print(f"{title_data[i]} - {artist_data[i]} - {country_data[i]} - {company_data[i]} - $ {price_data[i]} - {year_data[i]}")  
  
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
        print(catalog_data[increment])'''



        
def main():
    main_data = fetch_info()
    title_data = get_data_title(main_data)
    artist_data = get_data_artist(main_data)
    country_data = get_data_country(main_data)
    company_data = get_data_company(main_data)
    price_data = get_data_price(main_data)
    year_data = get_data_year(main_data)
    display_output(title_data,artist_data,country_data,company_data,price_data,year_data)
    
main()
