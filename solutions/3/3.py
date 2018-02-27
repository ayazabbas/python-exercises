import random


responses = ["rock", "paper", "scissors"] # create a list with the possible responses the program gives



# This function will take the user's input and assign a numerical value if it's rock (1),
# paper (2), and scissors (3), randomly choose a response (negative 1,2,3) then add the
# scores to determine the winner.

def compare(userInput):
    # These if..elif statements assign a value to the user's input
    if userInput == "rock":
        userValue = 1
    elif userInput == "paper":
        userValue = 2
    elif userInput == "scissors":
        userValue = 3
    else:
        return "Unrecognised input. Try again..."  # If the user types nonsense, stop the function here
    
    # In response to the user we choose a negative score where rock=-3, paper=-2, scissors=-1
    compValue = random.randint(-3, -1)
    
    # Do some trickery to go from the negative value to the correct index in the responses list (list indexes start from 0)
    print("I choose " + responses[(compValue * -1) - 1])

    result = userValue + compValue  # By adding these two values we can determine who the winner is

    # The result will range from -2 to 2, think about which values correspond to which outcome
    if result == 0:
        return "Draw!"
    elif result == -1 or result == 2:
        return "I win! Play again or type exit to stop."
    elif result == -2 or result == 1:
        return "You win! Play again or type exit to stop."


print("Type rock, paper or scissors to play. Type exit to stop.")
userInput = input()

while userInput != "exit":  # similar loop to the one in exercise 1
    print(compare(userInput))
    print()  # an empty print statement will put a blank line
    userInput = input()  # at the end of each iteration, get the user to input something else