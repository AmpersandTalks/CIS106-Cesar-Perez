# This program will print out a sentence in reverse and
# will also delete leading, trailing, and duplicate spaces.

def get_sentence():
    print("Enter Sentence to reverse it")
    name = str(input())
    name = name.strip()
    return name


def get_list(name):
    name_list = name.split()
    return name_list


def string_reverse(name):
    print(name[::-1])


def display_output(name_list):
    name_string = " ".join(name_list)
    print(" In reverse you string will look something like.....")
    string_reverse(name_string)


def main():
    name = get_sentence()
    name_list = get_list(name)
    display_output(name_list)


main()
