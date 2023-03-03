#this script creates a webbased game based on the game Simon Says. The game is played by pressing the buttons in the order that they light up. The game is over when the player presses the wrong button. The game is won when the player presses the correct button 20 times in a row.
#This game has a basic GUI that displays the score and the number of times the player has won. The GUI also has a button that allows the player to reset the game.
#The game is played by pressing the buttons in the order that they light up. The game is over when the player presses the wrong button. The game is won when the player presses the correct button 20 times in a row.

import tkinter as tk
import random
import time

#this function creates the GUI
def create_GUI():


#create the window
    window = tk.Tk()
    window.title("Simon Says")
    window.geometry("500x500")

#create the score label
    score_label = tk.Label(window, text = "Score: 0")
    score_label.grid(row = 0, column = 0)
    
#create the win label
    win_label = tk.Label(window, text = "Wins: 0")
    win_label.grid(row = 0, column = 1)

#create the reset button
    reset_button = tk.Button(window, text = "Reset", command = reset)
    reset_button.grid(row = 0, column = 2)

#create the buttons
    button1 = tk.Button(window, text = "1", command = lambda: button_press(1))
    button1.grid(row = 1, column = 0)
    button2 = tk.Button(window, text = "2", command = lambda: button_press(2))
    button2.grid(row = 1, column = 1)
    button3 = tk.Button(window, text = "3", command = lambda: button_press(3))
    button3.grid(row = 1, column = 2)
    button4 = tk.Button(window, text = "4", command = lambda: button_press(4))
    button4.grid(row = 1, column = 3)

#this function resets the game
def reset():

#reset the score and win variables
    global score
    global win
    score = 0
    win = 0

#reset the score and win labels
global score_label.config(text = "Score: 0")
global win_label.config(text = "Wins: 0")

#this function is called when a button is pressed
def button_press(button):

#check if the button pressed is the correct button
    if button == button_sequence[score]:
        global score
        score += 1
        score_label.config(text = "Score: " + str(score))
        if score == 20:
            global win
            win += 1
            win_label.config(text = "Wins: " + str(win))
            score = 0
            score_label.config(text = "Score: " + str(score))
            button_sequence.clear()
            create_button_sequence()
    else:
        score = 0
        score_label.config(text = "Score: " + str(score))
        button_sequence.clear()
        create_button_sequence()

#this function creates the button sequence
def create_button_sequence():

#add a random number between 1 and 4 to the button sequence
    button_sequence.append(random.randint(1,4))

#this function lights up the buttons in the button sequence
def light_up_buttons():

#light up the buttons in the button sequence
    for i in range(len(button_sequence)):
        if button_sequence[i] == 1:
            button1.config(bg = "red")
            window.update()
            time.sleep(0.5)
            button1.config(bg = "SystemButtonFace")
            window.update()
            time.sleep(0.5)
        elif button_sequence[i] == 2:
            button2.config(bg = "blue")
            window.update()
            time.sleep(0.5)
            button2.config(bg = "SystemButtonFace")
            window.update()
            time.sleep(0.5)
        elif button_sequence[i] == 3:
            button3.config(bg = "green")
            window.update()
            time.sleep(0.5)
            button3.config(bg = "SystemButtonFace")
            window.update()
            time.sleep(0.5)
        elif button_sequence[i] == 4:
            button4.config(bg = "yellow")
            window.update()
            time.sleep(0.5)
            button4.config(bg = "SystemButtonFace")
            window.update()
            time.sleep(0.5)

#this function is called when the game starts
def start_game():

#create the button sequence
    create_button_sequence()

#light up the buttons in the button sequence
    light_up_buttons()

#initialize the score and win variables
score = 0
win = 0

#create the button sequence
button_sequence = []

#create the GUI
create_GUI()

#start the game
start_game()

#start the GUI
window.mainloop()

#end of script

#end of script

#end of script