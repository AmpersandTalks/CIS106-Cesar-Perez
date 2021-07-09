# This program will read the address from a text file 
# and display each address in comma separated text format.


def check_file(file_name):
    try:
        file = open(file_name, "r")
        file.close()
        message = "Success"
    except:
        message = "Error"
    return message


def read_file(file_name):
    with open(file_name, "r") as file:
        file_data = file.read()
    return file_data


def display_data(file_data):
    address = file_data.split("\n")
    for interger in range(0, len(address), 1):
        address_comma = get_address(address[interger])
        print(address_comma)


def get_name(name):
    name_list = name.split(" ")
    name = name_list[1] + "," + name_list[0]
    return name


def get_address(address):
    separate_address = address.split("\n")
    address_comma = get_name(separate_address[0]) + ","
    address_comma = address_comma + separate_address[1] + ","
    state_split = separate_address[len(separate_address) - 1].split(",")
    address_comma = address_comma + state_split[0] + ","
    state_split[1] = state_split[1].strip()
    state_split = state_split[1].split()
    address_comma = address_comma + state_split[0] + "," + state_split[1]
    return address_comma


def main():
    file_name = "addresses.txt"
    file_status = check_file(file_name)
    if file_status == "Success":
        file_data = read_file(file_name)
        display_data(file_data)
    else:
        print("File does not exist , first create the file ")


main()
