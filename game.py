import random
from tkinter import *
from tkinter import ttk

user_wins = 0
computer_wins = 0
draws = 0

choices = ["rock", "paper", "scissors"]

def winner():
    global user_wins
    global computer_wins
    global draws

    # Get user's choice and generate computer's choice
    user_input = entry.get().lower()
    computer_input = random.choice(choices)

    if user_input not in choices:
        dispay.configure(text="incorrect option")
        return

    if user_input == computer_input:
        draws += 1
        dispay.configure(text="It's Draw!")
    elif (user_input == "rock" and computer_input == "scissors") or (user_input == "scissors" and computer_input == "paper") or (user_input == "paper" and computer_input == "rock"):
        user_wins += 1
        dispay.configure(text="You Win!")
    else:
        computer_wins += 1
        dispay.configure(text="Computer Win!")
    ttk.Label(frm, text="Score - User:{} Computer: {} Draws: {}".format(user_wins, computer_wins, draws)).grid(column=0, row=1)


# it's a GUI module
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

# Game title
ttk.Label(frm, text="Rock, Paper, Scissors Game").grid(column=0, row=0)
dispay = ttk.Label(frm, text=" ")
dispay.grid(column=1, row=0)
ttk.Label(frm, text="Score - User:{} Computer: {} Draws: {}".format(user_wins, computer_wins, draws)).grid(column=0, row=1)

# Quit button
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=0)

# User input entry field
entry = ttk.Entry(frm)
entry.grid(column=0, row=2)

# Submit button
ttk.Button(frm, text="Submit", command=winner).grid(column=1, row=2)

root.mainloop()
