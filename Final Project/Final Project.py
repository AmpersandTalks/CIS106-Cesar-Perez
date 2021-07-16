# This program gets data from a XML file from online 
# and display in requested way, it also check data validation.

import urllib.request


def get_information():
    breakfast_menu = "https://www.w3schools.com/xml/simple.xml"
    try:
        breakfast_menu = urllib.request.urlopen(breakfast_menu).read().decode()
        main_data = breakfast_menu.split("</food>")
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
    calories_data = []
    for increment in range(0, len(main_data)-1, 1):
        calories_data.append(get_array(main_data[increment], tag))
    return calories_data

def check_price(price):
    for increment in range(0, len(price), 1):
        try:
            price[increment] = float(price[increment])
        except:
            print(f"Invalid price data: price[{increment}] = {price[increment]}")
            price[increment] = 0.00
    return price
  
def display_output(name_data, price_data, description_data, calories_data):
    length = max(
            len(name_data), 
            len(price_data),
            len(description_data), 
            len(calories_data))

    if len(name_data) < length:
        print("Invalid data: missing names")
        return

    if len(price_data) < length:
        print("Invalid data: missing prices")
        return

    if len(description_data) < length:
        print("Invalid data: missing descriptions")
        return

    if len(calories_data) < length:
        print("Invalid data: missing calories")
        return

    for increment in range(len(name_data)):
        print(f"{name_data[increment]} - {description_data[increment]} - {calories_data[increment]} - $ {price_data[increment]}")

def get_data_average(price):
    total = 0
    for increment in range(0, len(price), 1):
        total = total + price[increment]
    average = total / len(price)
    return average

def display_output_average(record, average):
    print(f" Total Records Available in menu : {record}")
    print(f" Average price of items in menu  : {average :.2f}")

def main():
    main_data = get_information()
    name_data = get_data(main_data, "</name>")
    price_data = get_data(main_data, "</price>")
    price_data = check_price(price_data)
    description_data = get_data(main_data, "</description>")
    calories_data = get_data(main_data, "</calories>")
    display_output(name_data, price_data, description_data, calories_data)
    average_data = get_data_average(price_data)
    display_output_average(len(name_data), average_data)


main()
