import random

user_wins = 0
computer_wins = 0
draws = 0

choices = ["rock", "paper", "scissors"]

def winner(user_input, computer_input):
    global user_wins
    global computer_wins
    global draws
    if user_input== computer_input:
        draws += 1
        return "It's Draw!"
    elif (user_input == "rock" and computer_input == "scissors") or (user_input == "scissors" and computer_input == "paper") or (user_input == "paper" and computer_input == "rock"):
        user_wins += 1
        return "You Win!"
    else:
        computer_wins += 1
        return "Computer Win!"

while True:
    print("Rock, Paper, Scissors Game")
    print("Enter your choice (rock, paper, scissors) or 'q' to quit:")

    user_input = input().lower()

    if user_input == "q":
        break

    if user_input not in choices:
        print("Please give correct choice like rock, paper, scissors or q (to quit the game)")
        continue

    computer_input = random.choice(choices)

    result = winner(user_input, computer_input)

    print(result)
    print("Score - User:", user_wins, "Computer:", computer_wins, "Draws:", draws)
