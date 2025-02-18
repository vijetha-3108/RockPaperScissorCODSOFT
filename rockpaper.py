import tkinter as tk
import random

# Initialize user and computer scores
user_score = 0
computer_score = 0

# Function to play the game when a button is clicked
def play(user_choice):
    global user_score, computer_score

    # Stop game if a player has already won 3 rounds
    if user_score >= 3 or computer_score >= 3:
        return  

    # Randomly select Rock, Paper, or Scissors for the computer
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    # Determine winner and update the result label
    result = determine_winner(user_choice, computer_choice)

    # Update the choice labels
    user_label.config(text=f"Your Choice: {user_choice}", fg="#ffcc00")
    computer_label.config(text=f"Computer's Choice: {computer_choice}", fg="#ff6600")

    # Update result label color based on outcome
    if "You win" in result:
        result_label.config(text=result, fg="green")
        user_score += 1
    elif "You lose" in result:
        result_label.config(text=result, fg="red")
        computer_score += 1
    else:
        result_label.config(text=result, fg="blue")

    # Update the score label
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}", fg="#0099ff")

    # Check if someone has won the match
    if user_score == 3 or computer_score == 3:
        declare_winner()

# Function to determine winner based on choices
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "You lose!"

# Function to declare final winner when a player reaches 3 points
def declare_winner():
    if user_score == 3:
        result_label.config(text="🎉 You won the match! 🎉", fg="lightgreen")
    elif computer_score == 3:
        result_label.config(text="Computer wins the match!", fg="red")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_label.config(text="Your Choice: ", fg="white")
    computer_label.config(text="Computer's Choice: ", fg="white")
    result_label.config(text="Make your move!", fg="white")
    score_label.config(text="Score - You: 0 | Computer: 0", fg="white")

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors (First to 3 Wins)")
root.geometry("400x450")  # Keeping the original size
root.config(bg="#222222")  # Dark mode theme

# Centering the frame in the window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Frame to hold all the UI elements
frame = tk.Frame(root, bg="#222222")
frame.grid(row=0, column=0)

# Title label with padding
title_label = tk.Label(frame, text="Rock-Paper-Scissors (First to 3 Wins)", font=("Arial", 14, "bold"), bg="#222222", fg="white")
title_label.pack(pady=(20, 10))  # Extra padding from top

# Labels to display user and computer choices
user_label = tk.Label(frame, text="Your Choice: ", font=("Arial", 12), bg="#222222", fg="white")
user_label.pack(pady=5)

computer_label = tk.Label(frame, text="Computer's Choice: ", font=("Arial", 12), bg="#222222", fg="white")
computer_label.pack(pady=5)

# Label to display game results
result_label = tk.Label(frame, text="Make your move!", font=("Arial", 14, "bold"), bg="#222222", fg="white")
result_label.pack(pady=10)

# Label to display scores
score_label = tk.Label(frame, text="Score - You: 0 | Computer: 0", font=("Arial", 12), bg="#222222", fg="white")
score_label.pack(pady=10)

# Frame to organize buttons
button_frame = tk.Frame(frame, bg="#222222")
button_frame.pack(pady=15)

# Rock button
rock_button = tk.Button(button_frame, text="Rock 🪨", font=("Arial", 12), width=10, bg="#ff6666", fg="white", command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=5, pady=5)

# Paper button
paper_button = tk.Button(button_frame, text="Paper 📄", font=("Arial", 12), width=10, bg="#66ccff", fg="white", command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=5, pady=5)

# Scissors button
scissors_button = tk.Button(button_frame, text="Scissors ✂", font=("Arial", 12), width=10, bg="#99cc33", fg="white", command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=5, pady=5)

# Reset button
reset_button = tk.Button(frame, text="Reset Game", font=("Arial", 12), width=15, bg="black", fg="white", command=reset_game)
reset_button.pack(pady=10)

# Run the GUI loop
root.mainloop()
