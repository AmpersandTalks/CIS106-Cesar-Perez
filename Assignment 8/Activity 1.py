def forLoop(number, factor):
    print(" While loop multiplication from " + str(number) + " to " + str(factor) + " by 1 :")
    increment = 1
    product = number
    for increment in range(increment, factor + 1, 1):
        product = number * increment
        print(str(number) + " * " + str(increment) + " = " + str(product))

def getValue(name):
    print(" Enter " + name + " value: ")
    value = int(input())
    
    return value

# Main
# this program uses a loop to generate a list of multiplication expressions for a given value
number = getValue("number")
factor = getValue("factor")
forLoop(number, factor)
