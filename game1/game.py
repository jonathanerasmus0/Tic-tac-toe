from tkinter import *
import random

# Function to handle the next turn
def next_turn(row, column):
    global player

    # Check if the button is empty and no winner is declared
    if buttons[row][column]['text'] == "" and not check_winner():

        # Set the player's mark on the button
        buttons[row][column]['text'] = player

        # Check for a winner or a tie, and update the label accordingly
        if check_winner() == "Tie":
            label.config(text="Tie!")
        elif check_winner():
            label.config(text=(player + " wins"))
        else:
            # Switch to the next player's turn
            player = players[(players.index(player) + 1) % 2]
            label.config(text=(player + " turn"))

# Function to check if there's a winner or a tie
def check_winner():
    # Check rows for a win
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            mark_winner(row, 0, row, 1, row, 2)
            return True

    # Check columns for a win
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            mark_winner(0, column, 1, column, 2, column)
            return True

    # Check diagonals for a win
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        mark_winner(0, 0, 1, 1, 2, 2)
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        mark_winner(0, 2, 1, 1, 2, 0)
        return True

    # If there's no winner, check for a tie
    if not empty_spaces():
        return "Tie"

    return False

# Function to check if there are any empty spaces left on the board
def empty_spaces():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                return True
    return False

# Function to mark the winning combination
def mark_winner(r1, c1, r2, c2, r3, c3):
    buttons[r1][c1].config(bg="green")
    buttons[r2][c2].config(bg="green")
    buttons[r3][c3].config(bg="green")

# Function to start a new game
def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

# Create the main window
window = Tk()
window.title("Tic-Tac-Toe")
window.configure(bg="#3498db")  # Background color set to modern blue

# Initialize players and the current player
players = ["X", "O"]
player = random.choice(players)

# Create the game board buttons
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

# Create and pack the label for player's turn
label = Label(text=player + " turn", font=('consolas', 40), bg="#3498db", fg="white")
label.pack(side="top")

# Create and pack the restart button
reset_button = Button(text="restart", font=('consolas', 20), command=new_game, bg="#3498db", fg="white")
reset_button.pack(side="top")

# Create and pack the frame for the game board
frame = Frame(window, bg="#3498db")
frame.pack()

# Create buttons for the game board
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

# Start the main event loop
window.mainloop()
