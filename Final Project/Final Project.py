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

def get_array(record, tag):
    get_record = record.split("\n")
     data = "None"
    try:
        for increment in range(0,len(get_record), 1):
            if(get_record[increment].find(tag) > 0):
                start = get_record[increment].find(">") + 1
                end = get_record[increment].find(tag)
                data = get_record[increment][start:end]
    except:
        data = "None"
    return data
  
def get_data(main_data, tag):
    year_data = []
     for increment in range(0, len(main_data)-1, 1):
        year_data.append(get_array(main_data[increment], tag))
    return year_data

def check_price(price):
    for increment in range(0, len(price), 1):
        try:
            price[increment] = float(price[increment])
        except:
            price[increment] = 0.00
    return price
  
def display_output(title_data, artist_data, country_data, company_data, price_data, year_data):
    for increment in range (0, len(title_data), 1):
        print(f"{title_data[increment]} - {artist_data[increment]} - {country_data[increment]} - {company_data[increment]} - $ {price_data[increment]} - {year_data[increment]}")  
 
def get_data_average(price):
    total = 0
    for increment in range(0, len(price), 1):
        total = total + price[increment]
    average = total / len(price)
    return average

def display_output_average(record, average):
    print(f" Total Records Available in Catalog : {record}")
    print(f" Average price of items in Catalog  : {average :.2f}")

def main():
    main_data = fetch_info()
    title_data = get_data(main_data, "</TITLE>")
    artist_data = get_data(main_data, "</ARTIST>")
    country_data = get_data(main_data, "</COUNTRY>")
    company_data = get_data(main_data, "</COMPANY>")
    price_data = get_data(main_data, "</PRICE>")
    price_data = check_price(price_data)
    year_data = get_data(main_data, "</YEAR>")
    print_output(title_data, artist_data, country_data, company_data, price_data, year_data)
    average_data = get_data_average(price_data)
    print_output_average(len(title_data), average_data)
    
   
main()

