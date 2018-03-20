"""
bull_cows_player_guess
Simple game written in Python for Egress for their coding challenge

Author: Keiron Jelf
"""
import random

# This determines the size of the game, increasing this would increase the amount of digits to guess
number_of_digits = 4
# Main game-play loop
playing = True
# Used to prevent un-needed loops
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Generated target value
secret_sequence = []
# Storing the user input
input_sequence = []
# Used for scoring
total_cows = 0
total_bulls = 0

"""
generate_random_sequence
Generates a random 4 digit number for the player to guess
params: None
returns: None
"""
def generate_random_sequence():
    random_digits = []
    # Doing this to use one loop
    list_of_remaining_digits = digits.copy()
    for i in range(number_of_digits):
        # Pull from list of digits, allocate a new one every time
        index = random.randint(0, (len(list_of_remaining_digits)-1))
        random_digits.append(list_of_remaining_digits[index])
        list_of_remaining_digits.pop(index)
    return random_digits


"""
get_guess
Runs a loop for the player to input a 4 digit input, with error checking and validation
params: None
returns: None
"""
def get_guess():
    result = False
    valid_input = []
    valid_inputs_left = digits.copy()
    input_string = input("Please input your guess: ")
    for d in range(number_of_digits):
        # Using this to cover multiple errors
        try:
            if len(input_string) != number_of_digits:
                raise ValueError
            # Should throw exception if its not an int
            current_check = int(input_string[d])
            # Throws exception if its not available e.g a repeated number
            valid_in_list = valid_inputs_left.index(current_check)
            valid_input.append(valid_inputs_left[valid_in_list])
            valid_inputs_left.pop(valid_in_list)
        except Exception as error:
            print("Invalid input: please choose {0} unique numbers between 1-9.".format(number_of_digits))
            return result, valid_input
    if len(valid_input) is number_of_digits:
        result = True
        return result, valid_input
    return result, valid_input


"""
calculate_cows_bulls
Calculates the number of cows and bulls within the players guess
params: None
returns: None
"""
def calculate_cows_bulls():
    bulls = 0
    cows = 0
    for i in range(number_of_digits):
        # Pointless looping to search if its a bull
        if input_sequence[i] is secret_sequence[i]:
            bulls = bulls+1
            continue
        # Looping to check for cows
        for c in range(number_of_digits):
            if c is i:
                continue
            if input_sequence[i] is secret_sequence[c]:
                cows = cows+1
                break
    return cows, bulls


# Generate our random number
secret_sequence = generate_random_sequence()
# Feel free to uncomment this
# print(secret_sequence)
while playing:
    # Get a valid user input
    input_loop = False
    while input_loop is False:
        input_loop, input_sequence = get_guess()
    print("{0} Sequence results".format(input_sequence))
    # Generate the score
    total_cows, total_bulls = calculate_cows_bulls()
    print("{0} => Cows: {1} Bulls: {2}".format(''.join(str(i) for i in input_sequence), total_cows, total_bulls))
    # If we have the maximum bulls, end the game!
    if total_bulls is number_of_digits:
        print("Game over!")
        playing = False
