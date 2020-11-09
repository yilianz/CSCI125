import random
# use table to represent game rule
gamerule = [["Draw","Win","Lose"],["Lose","Draw","Win"],["Win","Lose","Draw"]]

# input from user
user = int(input("Please enter your choice: 0- Rock, 1-Paper, 2- Scissors"))
# random choice by computer
computer = random.randint(0,2)

# nice print out
choices = ["rock","paper","scissor"]

print(f"You choose {choices[user]}, Computer choose {choices[computer]},User {gamerule[computer][user]}")