
print("Input a message or type 'exit' to quit.")
# When the program reaches this next line it waits for the user to type something
# and stores the input in a variable
userInput = input()

# We use a while loop to keep executing the 3 lines it contains until the user inputs "exit"
while userInput != "exit":
    print("You just typed " + userInput)
    print("Type another message, or 'exit' to quit")
    userInput = input()  # At the end of each iteration we want to wait for the user to type something else

print("Program exiting...")  # This line gets executed when the while loop finishes