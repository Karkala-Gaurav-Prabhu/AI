from tkinter import *
from random import randint

root = Tk()
root.title("TicTacToe")
root.geometry("400x400")

global flag1
global flag2
global flag3
global flag4
global flag5
global flag6
global flag7
global flag8
global flag9

flag1=0
flag2=0
flag3=0
flag4=0
flag5=0
flag6=0
flag7=0
flag8=0
flag9=0

def user_click1(flag1):
    if flag1 == 0:
        btn1["text"] = "X"
        
        o = randint(1,9)
        while o==1:
            o = randint(1,9)
        if o != 1:
            flag1 = 1
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
    else:
        pass
        
        
def user_click2(flag2):
    if flag2 == 0:
        btn2["text"] = "X"
        
        o = randint(1,9)
        while o==2:
            o = randint(1,9)
        if o != 2:
            flag2 = 1
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
    else:
        pass

def user_click3(flag3):
    if flag3 == 0:
        btn3["text"] = "X"
        
        o = randint(1,9)
        while o==3:
            o = randint(1,9)
        if o != 3:
            flag3 = 1
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
    else:
        pass

def user_click4(flag4):
    if flag4 == 0:
        btn4["text"] = "X"
        
        o = randint(1,9)
        while o==4:
            o = randint(1,9)
        if o != 4:
            flag4 = 1
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
    else:
        pass

def user_click5(flag5):
    if flag5 == 0:
        btn5["text"] = "X"
        
        o = randint(1,9)
        while o==5:
            o = randint(1,9)
        if o != 5:
            flag5 = 1
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
    else:
        pass

def user_click6(flag6):
    if flag6 == 0:
        btn6["text"] = "X"
        
        o = randint(1,9)
        while o==6:
            o = randint(1,9)
        if o != 6:
            flag6 = 1
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
    else:
        pass

def user_click7(flag7):
    if flag7 == 0:
        btn7["text"] = "X"
        
        o = randint(1,9)
        while o==7:
            o = randint(1,9)
        if o != 7:
            flag7 = 1
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
    else:
        pass

def user_click8(flag8):
    if flag8 == 0:
        btn8["text"] = "X"
        
        o = randint(1,9)
        while o==8:
            o = randint(1,9)
        if o != 8:
            flag8 = 1
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
    else:
        pass

def user_click9(flag9):
    if flag9 == 0:
        btn9["text"] = "X"
        
        o = randint(1,9)
        while o==9:
            o = randint(1,9)
        if o != 9:
            flag9 = 1
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
    else:
        pass


btn1 = Button(root, text="-", height = 8, width = 18, command = lambda: user_click1(flag1))
btn1.grid(row = 0, column = 0)

btn2 = Button(root, text="-", height = 8, width = 18, command = lambda: user_click2(flag2))
btn2.grid(row = 0, column = 1)

btn3 = Button(root, text="-", height = 8, width = 18, command = lambda: user_click3(flag3))
btn3.grid(row = 0, column = 2)

btn4 = Button(root, text="-", height = 8, width = 18, command = lambda: user_click4(flag4))
btn4.grid(row = 1, column = 0)

btn5 = Button(root, text="-", height = 8, width = 18, command = lambda: user_click5(flag5))
btn5.grid(row = 1, column = 1)

btn6 = Button(root, text="-", height = 8, width = 18, command = lambda: user_click6(flag6))
btn6.grid(row = 1, column = 2)

btn7 = Button(root, text="-", height = 8, width = 18, command = lambda: user_click7(flag7))
btn7.grid(row = 2, column = 0)

btn8 = Button(root, text="-", height = 8, width = 18, command = lambda: user_click8(flag8))
btn8.grid(row = 2, column = 1)

btn9 = Button(root, text="-", height = 8, width = 18, command = lambda: user_click9(flag9))
btn9.grid(row = 2, column = 2)

root.mainloop()
