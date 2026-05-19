import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)
print(random_number)

while True:
    # Get user input
    user_input = input("Guess the number (between 1 and 100): ")

    # Validate user input
    if not user_input.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(user_input)

    # Check if the guess is correct
    if guess < random_number:
        print("Too low! Try again.")
    elif guess > random_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        break
