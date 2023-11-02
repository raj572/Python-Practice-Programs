import random
import tkinter as tk
from tkinter import ttk

def play_game(user_action):
    computer_action = random.choice(elemental_actions)

    if user_action == computer_action:
        result_label.config(text="It's a tie!")
    elif (user_action == 'Fire' and computer_action == 'Earth') or \
         (user_action == 'Earth' and computer_action == 'Water') or \
         (user_action == 'Water' and computer_action == 'Fire'):
        result_label.config(text='Congrats! You Won!')
        user_score_var.set(user_score_var.get() + 5)
        computer_score_var.set(computer_score_var.get() - 1)
    else:
        result_label.config(text='Oops! You lose :(')
        user_score_var.set(user_score_var.get() - 1)
        computer_score_var.set(computer_score_var.get() + 5)

    user_score_label.config(text=f'Your current score is {user_score_var.get()}')
    computer_score_label.config(text=f'Computer current score is {computer_score_var.get()}')

def reset_game():
    user_score_var.set(0)
    computer_score_var.set(0)
    result_label.config(text="")
    user_score_label.config(text="Your current score is 0")
    computer_score_label.config(text="Computer current score is 0")

elemental_actions = ['Fire', 'Water', 'Earth']

root = tk.Tk()
root.title("Elemental Clash Game")

user_score_var = tk.IntVar()
computer_score_var = tk.IntVar()

frame = ttk.Frame(root)
frame.grid(column=0, row=0, padx=10, pady=10)

fire_button = ttk.Button(frame, text="Fire", command=lambda: play_game('Fire'))
fire_button.grid(column=0, row=0)

water_button = ttk.Button(frame, text="Water", command=lambda: play_game('Water'))
water_button.grid(column=1, row=0)

earth_button = ttk.Button(frame, text="Earth", command=lambda: play_game('Earth'))
earth_button.grid(column=2, row=0)

reset_button = ttk.Button(frame, text="Reset", command=reset_game)
reset_button.grid(column=1, row=1)

result_label = ttk.Label(frame, text="")
result_label.grid(column=0, row=2, columnspan=3)

user_score_label = ttk.Label(frame, text="Your current score is 0")
user_score_label.grid(column=0, row=3)

computer_score_label = ttk.Label(frame, text="Computer current score is 0")
computer_score_label.grid(column=2, row=3)

root.mainloop()
