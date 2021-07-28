import random

user_pick = input("Pick Rock/Paper/Scissors: ")
action = ["rock", "paper", "scissors"]
computer_pick = random.choice(action)

if user_pick.lower() in ["rock", "paper", "scissors"]:
    print("User picked", user_pick.capitalize() + ", Computer picked", computer_pick.capitalize())
    if user_pick.lower() == computer_pick:
        print("Tie!")
    elif user_pick.lower() == "rock" and computer_pick == "paper":
        print("Computer win!")
    elif user_pick.lower() == "rock" and computer_pick == "scissors":
        print("User win!")
    elif user_pick.lower() == "paper" and computer_pick == "rock":
        print("User win!")
    elif user_pick.lower() == "paper" and computer_pick == "scissors":
        print("Computer win!")
    elif user_pick.lower() == "scissors" and computer_pick == "rock":
        print("Computer win!")
    elif user_pick.lower() == "scissors" and computer_pick == "paper":
        print("User win!")
else:
    print("Please enter a valid choice!")
    quit()