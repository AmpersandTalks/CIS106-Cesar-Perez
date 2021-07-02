# The program will ask user to pick a number between 1 - 100 
# and will try guuessing the mid point to find the correct number.


def get_answer(maximum_number, minimum_number):
    guess = []
    middle_number = get_midddle_number(minimum_number, maximum_number)
    while True:
        choice = get_choice(middle_number)
        if choice == 'l':
            guess = get_guess(guess, middle_number)
            minimum_number = middle_number
            middle_number = get_midddle_number(minimum_number, maximum_number)
        elif choice == 'h':
            guess = get_guess(guess, middle_number)
            maximum_number = middle_number
            middle_number = get_midddle_number(minimum_number, maximum_number)
        elif choice == 'e':
            guess = get_guess(guess, middle_number)
            break
    return guess


def get_midddle_number(minimum_number, maximum_number):
    middle_number = int((minimum_number + maximum_number) / 2)
    return middle_number


def get_guess(guess, new_guess):
    guess.append(new_guess)
    return guess


def get_choice(middle_number):
    print(" Enter 'l' if the number is lower than: " + str(middle_number))
    print(" Enter 'h' if the number is higher than :" + str(middle_number))
    print(" Enter 'e' if the number is equal to: " + str(middle_number))
    choice = str(input())
    return choice


def display_results(guess):
    print("Total Guess made : " + str(len(guess)))
    print("Total guesses attempted are below ")
    print(guess)


def main():
    print("Please select one number between 1 - 100")
    guess = get_answer(0, 100)
    display_results(guess)


main()
