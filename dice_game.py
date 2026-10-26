import os
import sys
from playsound3 import playsound
import random
import time

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

dicerollsfx = [resource_path("sounds/dice1.mp3"), resource_path("sounds/dice2.mp3"), resource_path("sounds/dice3.mp3"), resource_path("sounds/dice4.mp3"), resource_path("sounds/dice5.mp3")]

dicecolors = ["green", "purple", "blue", "orange"]
dicenumbers = [[3, 3, 3, 3, 3, 3], [0, 0, 4, 4, 4, 4], [1, 1, 1, 5, 5, 5], [2, 2, 2, 2, 6, 6]]

print("""Welcome to Professor Schmidt's dice gambling game! I'm Professor Schmidt, and I will be your opponent for today's game.
To begin, you must first select a die to use. Your options are:

Green dice: [3, 3, 3, 3, 3, 3]
Purple dice: [0, 0, 4, 4, 4, 4]
Blue dice: [1, 1, 1, 5, 5, 5]
Orange dice: [2, 2, 2, 2, 6, 6]
""")
playerchoice = input("Please input the color of your selected die.\n").lower()
while True:
    if playerchoice in dicecolors:
        break
    else:
        playerchoice = (input("Sorry, none of the dice seem to come in that color. Try inputting a color on the list above.\n")).lower()

playerdice = dicenumbers[dicecolors.index(playerchoice)]
if dicecolors.index(playerchoice) == 3:
    schmidtdice = dicenumbers[0]
    print(f"\nYou chose the orange die. Now it's my turn to choose a die, and I'll choose the green die.")
else:
    schmidtdice = dicenumbers[dicecolors.index(playerchoice) + 1]
    print(f"\nYou chose the {playerchoice} die. Now it's my turn to choose a die, and I'll choose the {dicecolors[dicecolors.index(playerchoice) + 1]} die.")

playerscore = 0
schmidtscore = 0
print("Now that we have both selected our dice, it is time to roll them!")
time.sleep(3)
for round in range(10):
    playerroll = random.randrange(0, 6)
    schmidtroll = random.randrange(0, 6)
    print(f"\nRound {round + 1}!\nRolling...")
    playsound(random.choice(dicerollsfx))
    time.sleep(random.randrange(1, 3))

    if playerdice[playerroll] > schmidtdice[schmidtroll]:
        playerscore += 1
        print(f"You rolled a {playerdice[playerroll]}. I rolled a {schmidtdice[schmidtroll]}. You win this round.")
    else:
        schmidtscore += 1
        print(f"You rolled a {playerdice[playerroll]}. I rolled a {schmidtdice[schmidtroll]}. I win this round.")
    time.sleep(3)

print(f"\nAnd now, it is time to tally up the scores.")
time.sleep(2)
print(f"Your score was {playerscore}")
time.sleep(2)
print(f"My score was {schmidtscore}")
time.sleep(2)
if playerscore == schmidtscore:
    print(f"We're tied! Thus, we must perform one last roll to determine the true winner.")
    time.sleep(2)
    print(f"\nRound 11!\nRolling...")
    playsound(random.choice(dicerollsfx))
    time.sleep(random.randrange(1, 3))
    if playerdice[playerroll] > schmidtdice[schmidtroll]:
        playerscore += 1
        print(f"You rolled a {playerdice[playerroll]}. I rolled a {schmidtdice[schmidtroll]}.")
        time.sleep(3)
    else:
        schmidtscore += 1
        print(f"You rolled a {playerdice[playerroll]}. I rolled a {schmidtdice[schmidtroll]}.")
        time.sleep(3)
if playerscore > schmidtscore:
    print(f"\nIt seems that you won! This is almost as bad as that time I lost to my CS 113 students two years in a row...")
    playsound(resource_path("sounds/victory.mp3"))
elif playerscore < schmidtscore:
    print(f"\nIt seems that I won! It's a good thing that probability doesn't require a math licsense to learn!")
    playsound(resource_path("sounds/defeat.mp3"))