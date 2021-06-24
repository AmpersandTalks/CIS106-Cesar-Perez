# This program uses nested loops to generate a multiplication table.


def get_value(name):
    print("Please enter " + name + " number")
    value = int(input())
    return value


def get_output(start, end):
    axis_x = start
    print("", end='\t')
    for axis_x in range(start, end + 1):
        print(str(axis_x), end='\t')


def get_table(start, end):
    axis_x = start
    for axis_x in range(start, end + 1):
        print("", end='\n')
        print(str(axis_x), end='\t')
        axis_y = start
        for axis_y in range(start, end + 1):
            print(str(axis_x * axis_y), end='\t')
    print()


def main():
    start = get_value("etart")
    end = get_value("end")
    get_output(start, end)
    get_table(start, end)

    
main()
