# -*- coding: utf-8 -*-

# simple program to ask user for rectangle dimensions and to output a rectangle of those dimensions as an .svg file. 

import turtle
#import tkinter as tk

def main():
    
    # get width and length from user - make this into a GUI later
    width = float(input('Enter a width for the rectangle:'))
    length = float(input('Enter a length for the rectangel:'))

    t = turtle.Turtle()
    
    t.pendown()
    t.forward(width)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(length)
    t.penup()

#    done()

main()
#t.save_as("rectangle.svg")

# #create a window for user inputs
# inputGUI = tk.Tk()
# inputGUI.title("Rectangle Dimensions")
# inputGUI.geometry("300x250")

# # ask user for width and length inputs
# widthPrompt = tk.Label(text = "Enter the width of the rectangle:")
# widthPrompt.grid()
# width = tk.Entry(inputGUI, width = 20)

# lengthPrompt = tk.Label(text = "Enter the length of the rectangle:")
# lengthPrompt.grid(row = 1, column = 0)
# length = tk.Entry(inputGUI, width = 20)

# inputGUI.mainloop()

