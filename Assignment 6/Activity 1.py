# This program calculates their weekly, monthly, and annual gross pay.
# References: https://en.wikibooks.org/wiki/JavaScript

def calculate_monthly(hours, rate_per_hour):
    monthly = hours * rate_per_hour * 4
    return monthly


def calculate_annual(hours, rate_per_hour):
    annual = hours * rate_per_hour * 52
    return annual


def calculate_weekly(hours, rate_per_hour):
    weekly = hours * rate_per_hour
    return weekly


def display_result(weekly, monthly, annual):
    print(str(weekly) + " weekly " +
    str(monthly) + " monthly " +
    str(annual) + " annually ")


def get_hours():
    print("Enter hours worked this week")
    hours = float(input())
    return hours


def get_rate_per_hour():
    print("Enter rate per hour")
    rate_per_hour = float(input())
    return rate_per_hour

# main function starts here

hours = get_hours()
rate_per_hour = get_rate_per_hour()
weekly = calculate_weekly(rate_per_hour, hours)
monthly = calculate_monthly(rate_per_hour, hours)
annual = calculate_annual(rate_per_hour, hours)
display_result(weekly, monthly, annual)
