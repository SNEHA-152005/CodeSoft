import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "You lose!"

# Function to play the game
def play_game(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(user_choice, computer_choice)
    
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1
    
    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score} Computer: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text=f"Score - You: {user_score} Computer: {computer_score}")

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Initialize scores
user_score = 0
computer_score = 0

# Create and place the widgets
instructions_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
instructions_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", command=lambda: play_game("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: play_game("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play_game("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

score_label = tk.Label(root, text=f"Score - You: {user_score} Computer: {computer_score}")
score_label.pack(pady=10)

reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=10)

# Run the application
root.mainloop()
