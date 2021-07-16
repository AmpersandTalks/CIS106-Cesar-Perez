# This program gets data from a XML file from online
# and display in requested way, it also check data validation.

import urllib.request


def get_information():
    url = "https://www.w3schools.com/xml/simple.xml"
    try:
        main_data = urllib.request.urlopen(url).read().decode()
        return main_data
    except:
        print("Error reading", url)
        exit(1)


def get_data(main_data, tag):
    array_data = []
    data = main_data.split("\n")
    for line in data:
        if tag not in line:
            continue

        start = line.find(">") + 1
        end = line.find("</")
        data = line[start:end]
        array_data.append(data)

    return array_data


def check_price(price):
    for increment in range(0, len(price), 1):
        try:
            price[increment] = float(price[increment])
        except:
            print(f"Invalid price data: price[{increment}] = " +
                f"{price[increment]}")
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
        print(f"{name_data[increment]} - {description_data[increment]} - " +
            f"{calories_data[increment]} - $ {price_data[increment]}")


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

    name_data = get_data(main_data, "name")
    price_data = get_data(main_data, "price")
    description_data = get_data(main_data, "description")
    calories_data = get_data(main_data, "calories")

    price_data = check_price(price_data)
    display_output(name_data, price_data, description_data, calories_data)
    average_data = get_data_average(price_data)
    display_output_average(len(name_data), average_data)


main()
