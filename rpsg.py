# import random

# possible_actions=["rock","paper","scissors"]

# while True:
#     user_action=input("enter a choice(rock,paper,scissors):").lower()

#     computer_action=random.choice(possible_actions)

#     print(f"\nyou chose {user_action},computer choice {computer_action}.\n")


# if user_action == computer_action:
#     print(f"both players selectes{user_action}.it tie")
# elif user_action=="rock":
#     if(computer_action=="scisssors"):
#         print("rock smashes scissors! you win!")
#     else:
#         print("Paper cover rocks! you lose")

# elif user_action=="paper":
#     if(computer_action=="rock"):
#         print("paper cover rocks! you win")
#     else:
#         print("scissors cuts paper! you lose!")

# elif user_action=="scissors":
#     if(computer_action=="paper"):
#         print("scisssors cut paper you win!")
#     else:
#         print("rock smashes scissors you lose!")\
        


# play_again = input("Play again? (yes/no): ")
# if play_again.lower() != "yes":
#     break

import random

possible_actions = ["rock", "paper", "scissors"]

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ").lower()

    if user_action not in possible_actions:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue

    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cut paper! You lose!")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cut paper! You win!")
        else:
            print("Rock smashes scissors! You lose!")

    # Ask the user if they want to play again
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
