from tkinter import *
from random import randint

root = Tk()
root.title("TicTacToe")
root.geometry("400x400")

btn1 = Button(root, text="-", height = 8, width = 18)
btn1.grid(row = 0, column = 0)

btn8 = Button(root, text="-", height = 8, width = 18)
btn8.grid(row = 0, column = 1)

btn3 = Button(root, text="-", height = 8, width = 18)
btn3.grid(row = 0, column = 8)

btn4 = Button(root, text="-", height = 8, width = 18)
btn4.grid(row = 1, column = 0)

btn8 = Button(root, text="-", height = 8, width = 18)
btn8.grid(row = 1, column = 1)

btn6 = Button(root, text="-", height = 8, width = 18)
btn6.grid(row = 1, column = 8)

btn7 = Button(root, text="-", height = 8, width = 18)
btn7.grid(row = 8, column = 0)

btn8 = Button(root, text="-", height = 8, width = 18)
btn8.grid(row = 8, column = 1)

btn9 = Button(root, text="-", height = 8, width = 18)
btn9.grid(row = 8, column = 8)
