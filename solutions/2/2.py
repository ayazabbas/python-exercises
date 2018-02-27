import random  # import random so we can use the randint() function

numbers = []  # Create an empty list
evenNumbers = []

while len(numbers) < 20:  # While the length of our list is less than 20
    numbers.append(random.randint(1, 100))  # Add a random number between 1 and 100 to the list

print(numbers)

# Here, we look at each element in the list one at a time and treat it as a variable 'x'
for x in numbers:
    if x % 2 == 0:  # Here we use the % operator to check if x is even or odd
        evenNumbers.append(x)  # If it's even we add it to the list, if not we do nothing and move on to the next element

print(evenNumbers)