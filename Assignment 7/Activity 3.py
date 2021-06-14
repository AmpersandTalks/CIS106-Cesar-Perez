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
    print("Would you like to use the US measurement system? Y or N ")
    choice = input()
    
    return choice

def get_miles():
    print("Enter a value for miles")
    miles = float(input())
    
    return miles

def metric_display_results(kilometers, meters, centimeters):
    print(str(kilometers) + " kilometers " + 
          str(meters) + " meters " + str(centimeters) + " centimeter ")

def process_metric():
    miles = get_miles()
    kilometers = calculate_kilometers(miles)
    meters = calculate_meters(miles)
    centimeters = calculate_centimeters(miles)
    metric_display_results(kilometers, meters, centimeters)

def process_us():
    miles = get_miles()
    yards = calculate_yards(miles)
    feet = calculate_centimeters(miles)
    inches = calculate_inches(miles)
    us_display_results(yards, feet, inches)

def us_display_results(yards, feet, inches):
    print(str(yards) + " yards " + 
          str(feet) + " feet " + str(inches) + " inches ")

# This program coverts the distance in miles into either the US system yards 
# or metric system kilometers.
choice = get_choice()
if choice == "Y" or choice == "y":
    process_us()
else:
    if choice == "N" or choice == "n":
        process_metric()
    else:
        print("Please enter Y to use the US measurement system or N to use the metric measurement system!")
