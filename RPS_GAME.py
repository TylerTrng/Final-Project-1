import random
from tkinter import *

def computer_play():
    #Allows Computer to randomly choose its play
    play_choice = ['rock','paper','scissor']
    computer_choice = random.choice(play_choice)
    label2.config(text='Computer: ' + str(computer_choice))
    return computer_choice
def game_play(value):
    #Once a RadioButton is clicked, the value will be retrieve and determine user's play based on the retrieved play
    global user
    if value == 0:
        user = 'scissor'
        label1.config(text='User: '+user)
        winner_check()
    elif value == 1:
        user = 'rock'
        label1.config(text='User: '+user)
        winner_check()
    elif value == 2:
        user = 'paper'
        label1.config(text='User: '+user)
        winner_check()
def winner_check():
    #This function will handle the result after both user and computer made their play
    #There are total 9 possible outcome, 3 times user will win, 3 times computer will win, and 3 time both tie
    global user, computer_score, user_score
    computer = computer_play()
    if user == 'rock' and computer == 'paper':
        print(f'Computer is {computer}. You are {user}. You lose')
        computer_score += 1
        computer_label.config(text='Computer: '+ str(computer_score))
    elif user == 'paper' and computer == 'rock':
        print(f'Computer is {computer}. You are {user}. You win')
        user_score += 1
        user_label.config(text='User: '+ str(user_score))
    elif user == 'scissor' and computer == 'paper':
        print(f'Computer is {computer}. You are {user}. You win')
        user_score += 1
        user_label.config(text='User: '+ str(user_score))
    elif user == 'paper' and computer == 'scissor':
        print(f'Computer is {computer}. You are {user}. You lose')
        computer_score += 1
        computer_label.config(text='Computer: '+ str(computer_score))
    elif user == 'rock' and computer == 'scissor':
        print(f'Computer is {computer}. You are {user}. You win')
        user_score += 1
        user_label.config(text='User: '+ str(user_score))
    elif user == 'scissor' and computer == 'rock':
        print(f'Computer is {computer}. You are {user}. You lose')
        computer_score += 1
        computer_label.config(text='Computer: '+ str(computer_score))
        
    elif user == 'scissor' and computer == 'scissor':
        print(f'Computer is {computer}. You are {user}. You tie')
    elif user == 'rock' and computer == 'rock':
        print(f'Computer is {computer}. You are {user}. You tie')
    elif user == 'paper' and computer == 'paper':
        print(f'Computer is {computer}. You are {user}. You tie')
root = Tk()
root.resizable(False,False)

#Init values needed to execute the code
var = IntVar()
var.set(0)
user = game_play(var)
label_name = Label(root, text='Rock - Paper - Scissor',bd=10, font=(25))
label_name.grid(column=1,row=0)
label1 = Label(root, text='User: ',bd=10, font=(25))
label1.grid(column=1, row = 1)
label2 = Label(root, text='Computer: ',bd=10, font=(25))
label2.grid(column=1, row = 2)

#This is the GUI's code
scissor_button = Radiobutton(root, text="Scissor", variable = var, value =0, command=lambda: game_play(var.get()), bd=10, font=(20))
scissor_button.grid(column = 1, row=3)
rock_button = Radiobutton(root, text="Rock", variable = var, value =1, command=lambda: game_play(var.get()), bd=10, font=(20))
rock_button.grid(column = 1, row=4)
paper_button = Radiobutton(root, text="Paper", variable = var, value =2 , command=lambda: game_play(var.get()), bd=10, font=(20))
paper_button.grid(column = 1, row=5)

#To keep track the score after each play, I initialize two variable user_score and computer_score
user_score = 0
computer_score = 0
computer_label = Label(root, text="Computer: "+ str(computer_score))
computer_label.grid(column=1, row=6)
user_label = Label(root, text="User: "+ str(user_score))
user_label.grid(column=1, row=7)
root.mainloop()



    
