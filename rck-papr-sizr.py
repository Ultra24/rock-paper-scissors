# Authored by Ultra24 09/29/21
import random

# asking for user input & generating random number
rock_paper_scissors = input("Enter either rock, paper, or scissors:")
generate_rand = random.randint(1,3)
print("The computer chose:", generate_rand)

# function for processing user's & computer's data in order to display results
def results():
    if rock_paper_scissors == "rock" and generate_rand == 3:
        print("The computer got scissors; You win!")
    elif rock_paper_scissors == "rock" and generate_rand == 2:
        print("The computer got paper; You lose.")
    elif rock_paper_scissors == "rock" and generate_rand == 1:
        print("The computer also got rock; You tied.")
    elif rock_paper_scissors == "paper" and generate_rand == 1:
        print("The computer got rock; You win!")
    elif rock_paper_scissors == "paper" and generate_rand == 3:
        print("The computer got scissors; You lose.")
    elif rock_paper_scissors == "paper" and generate_rand == 2:
        print("The computer also got scissors; You tied.")
    elif rock_paper_scissors == "scissors" and generate_rand == 1:
        print("The computer got rock; You lose.")
    elif rock_paper_scissors == "scissors" and generate_rand == 2:
        print("The computer got paper; You win!")
    elif rock_paper_scissors == "scissors" and generate_rand == 3:
        print("The computer also go scissors; You tied.")
    elif rock_paper_scissors == int:
        print("You inputted a number, try again and make sure to put either rock, paper, or scissors")

results()


retry = input("Would you like to play again? Y/N:")

if retry == "Y" or "y" or "yes" or "Yes" or "YES":
    print("Rebooting...")
elif retry == "N" or "n" or "no" or "No" or "NO":
    print("Have an excellent day!")


