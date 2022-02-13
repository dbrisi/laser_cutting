# -*- coding: utf-8 -*-

# simple program to ask user for rectangle dimensions and output a rectangle of those dimensions as an .svg file.

def main():

    # initialize maximum size (area), length and width of the rectangle
    #maxSize = 0
    height = 0
    width = 0
    initials = ""
    #tooBig = True # placeholder for initial while loop

    # one pixel = 1/96 inch
    inchToPix = 96;

    # one inch = 72 pt font size; conversion factor to fill much of the box (height or width)
    fontSizeConv = 72

    print("This program helps you create a user-defined rectangle with initials engraved on it.")
    print('The length and width of the rectangle cannot exceed 2".')
    # get maximum size, width and length from user
    # check the dimensions are valid and are less than or equal to the maximum size
    # while tooBig == True or height > 2 or width > 2:
    while height <= 0 or width <= 0 or height > 2 or width > 2:
        # while maxSize <= 0:
        #     maxSize = float(input('Enter a maximum size (in^2) for the rectangle: '))
        #     if maxSize <= 0:
        #         "Invalid maximum size!"
        while width <= 0 or width > 2:
            width = float(input('Enter a width (in) for the rectangle: '))
            if width <= 0:
                print("Invalid width! Only positive values accepted.")
            if width > 2:
                print('Invalid width! Must be less than or equal to 2"')
        while height <= 0 or height > 2:
            height = float(input('Enter a height (in) for the rectangle: '))
            if height <= 0:
                print("Invalid height! Only positive values accepted.")
            if height > 2:
                print('Invalid height! Must be less or equal to than 2"')
        # if height * width > maxSize:
        #     print("Exceeds maximum size of ", maxSize," in^2. Please try again.")
        #     print("-----------------------------------------------------")
        #     # set all variables to zero again
        #     tooBig = True
        #     maxSize = 0
        #     height = 0
        #     width = 0
        # else:
        #     tooBig = False

    # Ask user for initials
    while (len(initials) <= 0 or len(initials) > 3):
        initials = input("Enter your initials: ")
        if len(initials) > 3:
            print("That is a lot of initials. Try again. ")

    # adjust font size so that the text does not exceed the rectangle bounds
    if height < width:
        fontSize = fontSizeConv*(4/5)*height
    else:
        fontSize = fontSizeConv*(3/5)*width

    # ask user to name the file (no extension)
    fileNameInput = input("Enter a new file name (no extension): ")
    fileName = fileNameInput + ".svg"

    # output the dimensions of the rectanlge as an svg file
    f = open(fileName,"w")
    f.write('<?xml version = "1.0" encoding = "UTF-8" ?> \n')
    f.write('<svg xmlns="http://www.w3.org/2000/svg" version = "1.1"> \n')
    f.write(f'<rect x = "10" y = "10" width = "{width*inchToPix}" height = "{height*inchToPix}" stroke = "black" stroke-width = "2" fill = "none" /> \n')
    f.write(f'<text x = "{10 + (width*inchToPix)/2}" y = "{10 + (height*inchToPix)/2}" dominant-baseline= "central" text-anchor= "middle" font-size = "{fontSize}px" fill = "red">' + initials + ' </text> \n')
    f.write('</svg>')
    f.close()

main()
