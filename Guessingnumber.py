
import random  # Import the random module

# Define the range for the random number
lower_bound = 1  
upper_bound = 10
max_attempts = 10  

# Generate the random target number
target_number = random.randint(lower_bound, upper_bound)  

# Game loop
for attempt in range(max_attempts):
    try:
        guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))  
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue  # Skip to the next iteration if input is not a valid integer

    if guess < target_number:
        print("Too low! Try again.")
    elif guess > target_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {attempt + 1} attempts!")
        break  
else:
    print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {target_number}.")
