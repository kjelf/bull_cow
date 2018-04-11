"""
bulls_cows_permutations

This is a solution given to the bulls and cows programming problem given by egress.
Written by Keiron Jelf
"""
from itertools import permutations
from random import shuffle

# Some globals for game play
playing = True
valid_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
amount_of_guesses = 0

# Edit this if you want a more complicated game
amount_of_digits = 4

"""
user_score
Function to prompt the user to score a guess for the game - formatted like Bulls Cows eg. 01 40 31 etc..
Fully error checked, results in a list formatted for use with my functions.

:param None
:return result - A list of integers with the score
"""
def user_score():
    cows = 0
    bulls = 0
    inputting = True
    while inputting:
        try:
            input_string = input()
            if len(input_string) > 2 or len(input_string) < 2:
                raise ValueError
            # Should throw exception if its not an int
            current_check = int(input_string)
            cows = int(current_check % 10)
            bulls = int(current_check / 10)
            if cows > 4 or bulls > 4:
                raise ValueError
            if cows < 0 or bulls < 0:
                raise ValueError
            inputting = False
        except Exception as error:
            print("Invalid input: please enter a valid score e.g 12, 31, 04...")
    result = [cows, bulls]
    return result


"""
compatible_number
This function takes a list of numbers which are a possible answer still within our possible answers list. We then take 
that number sequence and compare it to the guess we used previously, scoring it based on the same bull and cow rules. 
If we score the same, we have a potential answer to add to back to our possible answers list.

:param numbertocheck - Set of numbers in a list of a potential number to be added to our potential number list
:param previousguess - The guess we had last, used to generate the check out number
:param scoreofprevious - List of scores we recieved from the user upon guessing, used to validate a number
:return boolean - Return if this number is valid given our results and previous result
"""

def compatible_number(numbertocheck, previousguess, scoreofprevious):
    cows = 0
    bulls = 0
    for i in range(len(previousguess)):
        if previousguess[i] == numbertocheck[i]:
            bulls += 1
        elif previousguess[i] in numbertocheck:
            cows += 1
    if scoreofprevious[0] is cows and scoreofprevious[1] is bulls:
        return True
    else:
        return False


# Create a list of all possible numbers
possible_answers = list(permutations(valid_digits, amount_of_digits))
# Randomise them - we do this to make it so the game isn't the same all the time!
shuffle(possible_answers)
# Playing loop...
print("Bulls and cows solver.\n"
      "I will guess your numbers, please score me giving me a number of cows and bulls!")
while playing:
    amount_of_guesses += 1
    # Get an answer from our list
    guess = possible_answers[0]
    print("Guess #{0}: {1}".format(amount_of_guesses, ''.join(str(i) for i in guess)))
    score = user_score()
    # If we get 4 bulls, we win!
    if score[1] == 4:
        print("I got it in {0} guesses!!".format(amount_of_guesses))
        playing = False
    # Take our list and remove any numbers that don't score the same
    possible_answers = [i for i in possible_answers if compatible_number(i, guess, score)]
    # This runs if the game is scored in-correctly as the list becomes empty
    if len(possible_answers) is 0:
        print("The game was not scored correctly, please re-run")
        playing = False
