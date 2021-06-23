# this program uses a loop to generate a list of multiplication expressions for a given value

def getValue(name):
    print(" Enter " + name + " value: ")
    value = int(input())
    return value


def displayExpression(number, increment, product):
    print(str(number) + " * " + str(increment) + " = " + str(product))

    
def processExpressions(number, factor):
    print(" While loop multiplication from " + str(number) + " to " + str(factor) + " by 1 :")
    increment = 1
    product = number
    while increment <= factor:
        product = number * increment
        displayExpression(number, increment, product)
        increment = increment + 1

        
def main():
    number = getValue("value")
    factor = getValue("expressions")
    processExpressions(number, factor)

    
main()
