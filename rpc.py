# importing all the required stuff 

from tkinter import *
from random import randint
from tkinter import ttk


# creating the GUI box

root = Tk()
root.title("Rock-Paper-Scissors")
root.geometry("1000x800")
root.config(bg="black")


# heading

welcome=Label(root, text="Welcome to Rock-Paper-Scissors", fg="white", font=("Agency FB", 24), bg="black", bd=0)
welcome.pack(pady=25)


# the images

rock = PhotoImage(file="img/rock.png")
paper = PhotoImage(file="img/paper.png")
scissors = PhotoImage(file="img/scissors.png")


#adding images to a list

image_list=[rock, paper, scissors]


#random number b/w 0 and 2

pick_number = randint(0,2)


# print the image(the option choosen by the computer)

image_label = Label(root, image=image_list[pick_number])
image_label.pack(pady=30)


# change(it will change the choice made by the computer)
# we are also defining the game loginc in this

def spin():

    # pick a random number

    pick_number = randint(0,2)


    # print the image

    image_label.config(image=image_list[pick_number])


    # Converting the dropdown options to number

    if user_choice.get() == "Rock":
        value = 0

    elif user_choice.get() == "Paper":
        value = 1

    elif user_choice.get() == "Scissors":
        value = 2

    else:
        output.config(text="Choose a valid option!!!!!!")


    # logic for win or lose
    # 0 = rock
    # 1 = paper
    # 2 = scissors

    if value == 0: # rock

        if pick_number == 0: # rock
            output.config(text="It's a Tie! Spin again .......")

        elif pick_number == 1: # paper
            output.config(text="You Lost!")

        elif pick_number == 2: # scissors
            output.config(text="You Won!")


    if value == 1: # paper

        if pick_number == 0: # rock
            output.config(text="You Won!")

        elif pick_number == 1: # paper
            output.config(text="It's a Tie! Spin again .......")

        elif pick_number == 2: # scissors
            output.config(text="You Lost!")


    if value == 2: # scissors

        if pick_number == 0: # rock
            output.config(text="You Lost!")

        elif pick_number == 1: # paper
            output.config(text="You Won!")

        elif pick_number == 2: # scissors
            output.config(text="It's a Tie! Spin again .......")


# making our choices

user_choice = ttk.Combobox(root, value=("Rock", "Paper", "Scissors"))
user_choice.current(0)
user_choice.pack(pady=20)


# change button

spin_button = Button(root, text="spin!", command=spin, fg="white", bg="black")
spin_button.pack(pady=10)

#exit button 

exit_button = Button(root, text="Exit", command=root.destroy, fg="black", bg="red")
exit_button.pack(pady=20)


# won or not

output = Label(root, text="", fg="white", font=("Agency FB", 18), bg="black", bd=0)
output.pack(pady=50)


root.mainloop()