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

# while True:
#     print("Rock, Paper, Scissors Game")
#     print("Enter your choice (rock, paper, scissors) or 'q' to quit:")

#     user_input = input().lower()

#     if user_input == "q":
#         break

#     if user_input not in choices:
#         print("Please give correct choice like rock, paper, scissors or q (to quit the game)")
#         continue

#     computer_input = random.choice(choices)

#     result = winner(user_input, computer_input)

#     print(result)
#     print("Score - User:", user_wins, "Computer:", computer_wins, "Draws:", draws)


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Rock, Paper, Scissors Game").grid(column=0, row=0)
dispay = ttk.Label(frm, text=" ")
dispay.grid(column=1, row=0)
ttk.Label(frm, text="Score - User:{} Computer: {} Draws: {}".format(user_wins, computer_wins, draws)).grid(column=0, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=0)
entry = ttk.Entry(frm)
entry.grid(column=0, row=2)
ttk.Button(frm, text="Submit", command=winner).grid(column=1, row=2)
root.mainloop()
