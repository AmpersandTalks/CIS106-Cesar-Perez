# Program takes first name and last name from user and
# changes the forma to last_name, First Initial.
# Reference:
# https://www.w3schools.com/python/python_ref_string.asp


def get_name():
    print("Enter Your First Name and Last Name in one line text format")
    while True:
        name = str(input())
        name = name.strip()
        name_list = name.split()
        error = check_name(name_list, name)
        if error == "success":
            break

        print(" input is incorrect please try again")
    return name_list


def check_name(name_list, name):
    if name.isalpha() == "False":
        error = "fail"
    elif len(name_list) == 2:
        error = "success"
    else:
        error = "fail"
    return error


def get_first_name(name_list):
    first_name = name_list[0].capitalize()
    return first_name


def get_last_name(name_list):
    last_name = name_list[1].capitalize()
    return last_name


def display_output(first_name, last_name):
    print(last_name + ", " + first_name[0] + ". ")


def main():
    name_list = get_name()
    first_name = get_first_name(name_list)
    last_name = get_last_name(name_list)
    display_output(first_name, last_name)


main()
