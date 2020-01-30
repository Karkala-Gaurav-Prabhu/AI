from tkinter import *
from random import randint

root = Tk()
root.title("TicTacToe")
root.geometry("400x400")

def user_click1():
    btn1["text"] = "X"
    o = randint(1,9)
    if o != 1:
        if o == 2:
            btn2["text"] = "O"
        if o == 3:
            btn3["text"] = "O"
        if o == 4:
            btn4["text"] = "O"
        if o == 5:
            btn5["text"] = "O"
        if o == 6:
            btn6["text"] = "O"
        if o == 7:
            btn7["text"] = "O"
        if o == 8:
            btn8["text"] = "O"
        if o == 9:
            btn9["text"] = "O"
        
def user_click2():
    btn2["text"] = "X"
     o = randint(1,9)
    if o != 2:
        if o == 1:
            btn1["text"] = "O"
        if o == 3:
            btn3["text"] = "O"
        if o == 4:
            btn4["text"] = "O"
        if o == 5:
            btn5["text"] = "O"
        if o == 6:
            btn6["text"] = "O"
        if o == 7:
            btn7["text"] = "O"
        if o == 8:
            btn8["text"] = "O"
        if o == 9:
            btn9["text"] = "O"

def user_click3():
    btn3["text"] = "X"
     o = randint(1,9)
    if o != 3:
        if o == 2:
            btn2["text"] = "O"
        if o == 1:
            btn1["text"] = "O"
        if o == 4:
            btn4["text"] = "O"
        if o == 5:
            btn5["text"] = "O"
        if o == 6:
            btn6["text"] = "O"
        if o == 7:
            btn7["text"] = "O"
        if o == 8:
            btn8["text"] = "O"
        if o == 9:
            btn9["text"] = "O"

def user_click4():
    btn4["text"] = "X"
     o = randint(1,9)
    if o != 4:
        if o == 2:
            btn2["text"] = "O"
        if o == 3:
            btn3["text"] = "O"
        if o == 1:
            btn1["text"] = "O"
        if o == 5:
            btn5["text"] = "O"
        if o == 6:
            btn6["text"] = "O"
        if o == 7:
            btn7["text"] = "O"
        if o == 8:
            btn8["text"] = "O"
        if o == 9:
            btn9["text"] = "O"

def user_click5():
    btn5["text"] = "X"
     o = randint(1,9)
    if o != 5:
        if o == 2:
            btn2["text"] = "O"
        if o == 3:
            btn3["text"] = "O"
        if o == 4:
            btn4["text"] = "O"
        if o == 1:
            btn1["text"] = "O"
        if o == 6:
            btn6["text"] = "O"
        if o == 7:
            btn7["text"] = "O"
        if o == 8:
            btn8["text"] = "O"
        if o == 9:
            btn9["text"] = "O"

def user_click6():
    btn6["text"] = "X"
     o = randint(1,9)
    if o != 6:
        if o == 2:
            btn2["text"] = "O"
        if o == 3:
            btn3["text"] = "O"
        if o == 4:
            btn4["text"] = "O"
        if o == 5:
            btn5["text"] = "O"
        if o == 1:
            btn1["text"] = "O"
        if o == 7:
            btn7["text"] = "O"
        if o == 8:
            btn8["text"] = "O"
        if o == 9:
            btn9["text"] = "O"

def user_click7():
    btn7["text"] = "X"
     o = randint(1,9)
    if o != 7:
        if o == 2:
            btn2["text"] = "O"
        if o == 3:
            btn3["text"] = "O"
        if o == 4:
            btn4["text"] = "O"
        if o == 5:
            btn5["text"] = "O"
        if o == 6:
            btn6["text"] = "O"
        if o == 1:
            btn1["text"] = "O"
        if o == 8:
            btn8["text"] = "O"
        if o == 9:
            btn9["text"] = "O"

def user_click8():
    btn8["text"] = "X"
     o = randint(1,9)
    if o != 8:
        if o == 2:
            btn2["text"] = "O"
        if o == 3:
            btn3["text"] = "O"
        if o == 4:
            btn4["text"] = "O"
        if o == 5:
            btn5["text"] = "O"
        if o == 6:
            btn6["text"] = "O"
        if o == 7:
            btn7["text"] = "O"
        if o == 1:
            btn1["text"] = "O"
        if o == 9:
            btn9["text"] = "O"

def user_click9():
    btn9["text"] = "X"
     o = randint(1,9)
    if o != 9:
        if o == 2:
            btn2["text"] = "O"
        if o == 3:
            btn3["text"] = "O"
        if o == 4:
            btn4["text"] = "O"
        if o == 5:
            btn5["text"] = "O"
        if o == 6:
            btn6["text"] = "O"
        if o == 7:
            btn7["text"] = "O"
        if o == 8:
            btn8["text"] = "O"
        if o == 1:
            btn1["text"] = "O"


btn1 = Button(root, text="-", height = 8, width = 18, command = user_click1)
btn1.grid(row = 0, column = 0)

btn2 = Button(root, text="-", height = 8, width = 18, command = user_click2)
btn2.grid(row = 0, column = 1)

btn3 = Button(root, text="-", height = 8, width = 18, command = user_click3)
btn3.grid(row = 0, column = 2)

btn4 = Button(root, text="-", height = 8, width = 18, command = user_click4)
btn4.grid(row = 1, column = 0)

btn5 = Button(root, text="-", height = 8, width = 18, command = user_click5)
btn5.grid(row = 1, column = 1)

btn6 = Button(root, text="-", height = 8, width = 18, command = user_click6)
btn6.grid(row = 1, column = 2)

btn7 = Button(root, text="-", height = 8, width = 18, command = user_click7)
btn7.grid(row = 2, column = 0)

btn8 = Button(root, text="-", height = 8, width = 18, command = user_click8)
btn8.grid(row = 2, column = 1)

btn9 = Button(root, text="-", height = 8, width = 18, command = user_click9)
btn9.grid(row = 2, column = 2)

