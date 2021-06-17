def getValue(name):
    print(" Enter " + name + " value: ")
    value = int(input())
    
    return value

def whileLoop(number, factor, increment):
    print(" While loop multiplication from " + str(number) + " to " + str(factor) + " by " + str(increment) + " : ")
    product = number
    while increment <= factor:
        product = number * increment
        print(str(number) + " * " + str(increment) + " = " + str(product))
        increment = increment + 1

# this program uses a loop to generate a list of multiplication expressions for a given value
main():
    number = getValue("number")
    factor = getValue("factor")
    increment = 1
    whileLoop(number, factor, increment)
    
main()
