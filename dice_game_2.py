import os
import sys
from playsound3 import playsound
import random
import time
import tkinter as tk
from threading import Thread

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

dicerollsfx = [resource_path("sounds/dice1.mp3"), resource_path("sounds/dice2.mp3"), resource_path("sounds/dice3.mp3"), resource_path("sounds/dice4.mp3"), resource_path("sounds/dice5.mp3")]










def gametime():
    global dicerollsfx
    global playerdice
    global schmidtdice
    time.sleep(2)
    playerscore = 0
    schmidtscore = 0
    subtext.configure(state="normal")
    subtext.delete("1.0", "end")
    subtext.insert("1.0", "Now that we have both selected our dice, it is time to roll them!")
    subtext.tag_add("center", "1.0", "end")
    subtext.configure(state="disabled")
    time.sleep(3)
    for round in range(10):
        playerroll = random.randrange(0, 6)
        schmidtroll = random.randrange(0, 6)
        subtext.configure(state="normal")
        subtext.delete("3.0", "end")
        subtext.insert("end", f"\n\nRound {round + 1}!\nRolling...")
        subtext.configure(state="disabled")
        subtext.tag_add("center", "1.0", "end")
        playsound(random.choice(dicerollsfx))
        time.sleep(random.randrange(1, 3))
        if playerdice[playerroll] > schmidtdice[schmidtroll]:
            playerscore += 1
            subtext.configure(state="normal")
            subtext.insert("end", f"\n\nYou rolled a {playerdice[playerroll]}. I rolled a {schmidtdice[schmidtroll]}. You win this round.")
            subtext.configure(state="disabled")
            subtext.tag_add("green", "6.30", "end")
        else:
            schmidtscore += 1
            subtext.configure(state="normal")
            subtext.insert("end", f"\n\nYou rolled a {playerdice[playerroll]}. I rolled a {schmidtdice[schmidtroll]}. I win this round.")
            subtext.configure(state="disabled")
            subtext.tag_add("red", "6.30", "end")
        time.sleep(3)
    subtext.configure(state="normal")
    subtext.delete("1.0", "end")
    subtext.insert("end", "And now, it is time to tally up the scores!")
    subtext.configure(state="disabled")
    subtext.tag_add("center", "1.0", "end")
    time.sleep(2)
    subtext.configure(state="normal")
    subtext.insert("end", f"\n\nYour score was {playerscore}.")
    subtext.configure(state="disabled")
    time.sleep(2)
    subtext.configure(state="normal")
    subtext.insert("end", f"\n\nMy score was {schmidtscore}.")
    subtext.configure(state="disabled")
    time.sleep(2)
    if playerscore == schmidtscore:
        subtext.configure(state="normal")
        subtext.insert("end", "\n\nWe're tied! Thus, we must perform one last roll to determine the true winner.")
        subtext.configure(state="disabled")
        time.sleep(2)
        subtext.configure(state="normal")
        subtext.insert("end", f"\n\nRound 11!\nRolling...")
        playsound(random.choice(dicerollsfx))
        time.sleep(random.randrange(1, 3))
        if playerdice[playerroll] > schmidtdice[schmidtroll]:
            playerscore += 1
        else:
            schmidtscore += 1
        subtext.configure(state="normal")
        subtext.insert("end", f"\nYou rolled a {playerdice[playerroll]}. I rolled a {schmidtdice[schmidtroll]}.")
        subtext.configure(state="disabled")
        time.sleep(3)
    subtext.configure(state="normal")
    subtext.delete("1.0", "end")
    if playerscore > schmidtscore:
        subtext.insert("end", "It seems that you won!\nThis is almost as bad as that time I lost to my CS 113 students two years in a row...")
        subtext.configure(state="disabled")
        subtext.tag_add("center", "1.0", "end")
        subtext.tag_add("green", "1.0", "1.22")
        playsound(resource_path("sounds/victory.mp3"))
    elif playerscore < schmidtscore:
        subtext.insert("end", "It seems that I won!\nIt's a good thing that probability doesn't require a math license to learn!")
        subtext.configure(state="disabled")
        subtext.tag_add("center", "1.0", "end")
        subtext.tag_add("red", "1.0", "1.20")
        playsound(resource_path("sounds/defeat.mp3"))








def greenthread():
    thread = Thread(target=greenbuttonclick, daemon=True)
    thread.start()

def purplethread():
    thread = Thread(target=purplebuttonclick, daemon=True)
    thread.start()

def bluethread():
    thread = Thread(target=bluebuttonclick, daemon=True)
    thread.start()

def orangethread():
    thread = Thread(target=orangebuttonclick, daemon=True)
    thread.start()




def greenbuttonclick():
    global buttonframe
    buttonframe.destroy()
    global playerdice
    global schmidtdice
    playerdice = [3, 3, 3, 3, 3, 3]
    schmidtdice = [0, 0, 4, 4, 4, 4]
    subtext.configure(state="normal", height=12)
    subtext.insert("end", "\n\nYou chose the green die. Now it's my turn to choose a die, and I'll choose the purple die.")
    subtext.configure(state="disabled")
    subtext.tag_add("green", "12.14", "12.19")
    subtext.tag_add("purple", "12.79", "12.85")
    gametime()

def purplebuttonclick():
    global buttonframe
    buttonframe.destroy()
    global playerdice
    global schmidtdice
    playerdice = [0, 0, 4, 4, 4, 4]
    schmidtdice = [1, 1, 1, 5, 5, 5]
    subtext.configure(state="normal", height=12)
    subtext.insert("end", "\n\nYou chose the purple die. Now it's my turn to choose a die, and I'll choose the blue die.")
    subtext.configure(state="disabled")
    subtext.tag_add("purple", "12.14", "12.20")
    subtext.tag_add("blue", "12.80", "12.84")
    gametime()
    
def bluebuttonclick():
    global buttonframe
    buttonframe.destroy()
    global playerdice
    global schmidtdice
    playerdice = [1, 1, 1, 5, 5, 5]
    schmidtdice = [2, 2, 2, 2, 6, 6]
    subtext.configure(state="normal", height=12)
    subtext.insert("end", "\n\nYou chose the blue die. Now it's my turn to choose a die, and I'll choose the orange die.")
    subtext.configure(state="disabled")
    subtext.tag_add("blue", "12.14", "12.18")
    subtext.tag_add("orange", "12.78", "12.84")
    gametime()

def orangebuttonclick():
    global buttonframe
    buttonframe.destroy()
    global playerdice
    global schmidtdice
    playerdice = [2, 2, 2, 2, 6, 6]
    schmidtdice = [3, 3, 3, 3, 3, 3]
    subtext.configure(state="normal", height=12)
    subtext.insert("end", "\n\nYou chose the orange die. Now it's my turn to choose a die, and I'll choose the green die.")
    subtext.configure(state="disabled")
    subtext.tag_add("orange", "12.14", "12.20")
    subtext.tag_add("green", "12.80", "12.85")
    gametime()

root = tk.Tk()
root.title("Professor Schmidt's Dice Game")
root.geometry("900x700")
root.columnconfigure(1, weight=1)
root.configure(bg="#D3D3D3")

title = tk.Label(root, text="Welcome to Professor Schmidt's\nDice game!", font=("Comic Sans MS", 28), background="#D3D3D3")
title.grid(row=0, column=1)

subtext = tk.Text(root, height=10, width=30, bd=0, highlightthickness=0, bg=root.cget("bg"), font=("Comic Sans MS", 15))
subtext.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
subtext.insert("1.0", """I'm Professor Schmidt, and I will be your opponent for today's game.
To begin, you must first select a die to use.
Your options are:

Green dice: [3, 3, 3, 3, 3, 3]
Purple dice: [0, 0, 4, 4, 4, 4]
Blue dice: [1, 1, 1, 5, 5, 5]
Orange dice: [2, 2, 2, 2, 6, 6]

Please choose the die you wish to use.""")
subtext.configure(state="disabled")
subtext.tag_configure("center", justify="center")
subtext.tag_add("center", "1.0", "end")

subtext.tag_configure("green", foreground="#69d43d")
subtext.tag_configure("purple", foreground="#7a1aa9")
subtext.tag_configure("blue", foreground="#5daff9")
subtext.tag_configure("orange", foreground="#ea8a31")
subtext.tag_configure("red", foreground="#e32720")

subtext.tag_add("green", "5.0", "5.5")
subtext.tag_add("purple", "6.0", "6.6")
subtext.tag_add("blue", "7.0", "7.4")
subtext.tag_add("orange", "8.0", "8.6")

buttonframe = tk.Frame()
buttonframe.grid(row=2, column=1)
buttonframe.columnconfigure(0, weight=1)
buttonframe.rowconfigure(0, weight=1)
buttonframe.configure(bg="#D3D3D3")


greenbutton = tk.Button(buttonframe, text="Green", background="#69d43d", font=("Comic Sans MS", 12), width=6, command=greenthread)
greenbutton.grid(row=0, column=0, padx=10, pady=10)

purplebutton = tk.Button(buttonframe, text="Purple", background="#7a1aa9", font=("Comic Sans MS", 12), width=6, command=purplethread)
purplebutton.grid(row=0, column=1)

bluebutton = tk.Button(buttonframe, text="Blue", background="#5daff9", font=("Comic Sans MS", 12), width=6, command=bluethread)
bluebutton.grid(row=1, column=0)

orangebutton = tk.Button(buttonframe, text="Orange", background="#ea8a31", font=("Comic Sans MS", 12), width=6, command=orangethread)
orangebutton.grid(row=1, column=1)

quit = tk.Button(root, text="QUIT", command=root.destroy)
quit.grid(row=3, column=1, pady=30)

root.mainloop()