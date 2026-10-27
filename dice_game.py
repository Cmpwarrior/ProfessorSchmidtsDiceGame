import os
import sys
from playsound3 import playsound
import random
import time

RED = "\x1b[38;5;196m"
GREEN = "\x1b[38;5;40m"
PURPLE = "\x1b[38;5;91m"
BLUE = "\x1b[38;5;39m"
ORANGE = "\x1b[38;5;208m"
RESET = "\x1b[0m"

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


dicerollsfx = [resource_path("sounds/dice1.mp3"), resource_path("sounds/dice2.mp3"), resource_path("sounds/dice3.mp3"), resource_path("sounds/dice4.mp3"), resource_path("sounds/dice5.mp3")]

dicecolors = ["green", "purple", "blue", "orange"]
dicecolorsshort = ["g", "p", "b", "o"]
dicenumbers = [[3, 3, 3, 3, 3, 3], [0, 0, 4, 4, 4, 4], [1, 1, 1, 5, 5, 5], [2, 2, 2, 2, 6, 6]]
textcolors = [GREEN, PURPLE, BLUE, ORANGE]

print(f"""Welcome to Professor Schmidt's dice gambling game! I'm Professor Schmidt, and I will be your opponent for today's game.
To begin, you must first select a die to use. Your options are:

{GREEN}Green{RESET} dice: [3, 3, 3, 3, 3, 3]
{PURPLE}Purple{RESET} dice: [0, 0, 4, 4, 4, 4]
{BLUE}Blue{RESET} dice: [1, 1, 1, 5, 5, 5]
{ORANGE}Orange{RESET} dice: [2, 2, 2, 2, 6, 6]
""")
playerchoice = input("Please input the color of your selected die.\n").lower()
while True:
    if playerchoice in dicecolors:
        playerdice = dicenumbers[dicecolors.index(playerchoice)]
        break
    elif playerchoice in dicecolorsshort:
        playerdice = dicenumbers[dicecolorsshort.index(playerchoice)]
        break
    else:
        playerchoice = (input("\nSorry, none of the dice seem to come in that color. Try inputting a color on the list above.\n")).lower()

if dicenumbers.index(playerdice) == 3:
    schmidtdice = dicenumbers[0]
    print(f"\nYou chose the {ORANGE}orange{RESET} die. Now it's my turn to choose a die, and I'll choose the {GREEN}green{RESET} die.")
else:
    schmidtdice = dicenumbers[dicenumbers.index(playerdice) + 1]
    print(f"\nYou chose the {textcolors[dicenumbers.index(playerdice)]}{dicecolors[dicenumbers.index(playerdice)]}{RESET} die. Now it's my turn to choose a die, and I'll choose the {textcolors[dicenumbers.index(playerdice) + 1]}{dicecolors[dicenumbers.index(playerdice) + 1]}{RESET} die.")

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
        print(f"You rolled a {playerdice[playerroll]}. I rolled a {schmidtdice[schmidtroll]}. {GREEN}You win this round.{RESET}")
    else:
        schmidtscore += 1
        print(f"You rolled a {playerdice[playerroll]}. I rolled a {schmidtdice[schmidtroll]}. {RED}I win this round.{RESET}")
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
    print(f"\n{GREEN}It seems that you won!{RESET} This is almost as bad as that time I lost to my CS 113 students two years in a row...")
    playsound(resource_path("sounds/victory.mp3"))
elif playerscore < schmidtscore:
    print(f"\n{RED}It seems that I won!{RESET} It's a good thing that probability doesn't require a math licsense to learn!")
    playsound(resource_path("sounds/defeat.mp3"))