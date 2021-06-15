# This program coverts the distance in miles 
# into either the US system yards or metric system kilometers.


def calculate_centimeters(miles):
    centimeters = miles * 160934
    return centimeters


def calculate_feet(miles):
    feet = miles * 5280
    return feet


def calculate_inches(miles):
    inches = miles * 63360
    return inches


def calculate_kilometers(miles):
    kilometers = miles * 1.60934
    return kilometers


def calculate_meters(miles):
    meters = miles * 1609.34
    return meters


def calculate_yards(miles):
    yards = miles * 1760
    return yards


def get_choice():
    print("Would you like to use the US measurement system or Metric ?")
    choice = input()
    return choice


def get_miles():
    print("Enter a value for miles")
    miles = float(input())
    return miles


def metric_display_results(kilometers, meters, centimeters):
    print(str(kilometers) + " kilometers " + 
    str(meters) + " meters " + str(centimeters) + " centimeter ")


def process_metric(miles):
    kilometers = calculate_kilometers(miles)
    meters = calculate_meters(miles)
    centimeters = calculate_centimeters(miles)
    metric_display_results(kilometers, meters, centimeters)


def process_us(miles):
    yards = calculate_yards(miles)
    feet = calculate_centimeters(miles)
    inches = calculate_inches(miles)
    us_display_results(yards, feet, inches)


def us_display_results(yards, feet, inches):
    print(str(yards) + " yards " + 
    str(feet) + " feet " + str(inches) + " inches ")


def main():
    miles = get_miles()
    choice = get_choice()
    if choice == "US" or choice == "Us":
        process_us(miles)
    else:
        if choice == "Metric" or choice == "metric":
            process_metric(miles)
        else:
            print("Please enter US or metric to use that metric measurement system !")


main()
