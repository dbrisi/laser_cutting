# -*- coding: utf-8 -*-

# simple program to ask user for rectangle dimensions and to output a rectangle of those dimensions as an .svg file. 

def main():

    # initialize maximum size (area), length and width of the rectangle
    maxSize = 0
    length = 0
    width = 0
    tooBig = True # placeholder for initial while loop

    # one pixel = 1/96 inch
    inchToPix = 96; 

    # get maximum size, width and length from user
    # check the dimensions are valid and are less than or equal to the maximum size
    while tooBig == True:
        while maxSize <= 0:
            maxSize = float(input('Enter a maximum size (in^2) for the rectangle: '))
            if maxSize <= 0:
                "Invalid maximum size!"
        while width <= 0:
            width = float(input('Enter a width (in) for the rectangle: '))
            if width <= 0:
                "Invalid width!"
        while length <= 0:
            length = float(input('Enter a length (in) for the rectangle: '))
            if length <= 0:
                "Invalid length!"
        if length * width > maxSize:
            print("Exceeds maximum size of ", maxSize," in^2. Please try again.")
            print("-----------------------------------------------------")
            # set all variables to zero again
            tooBig = True
            maxSize = 0
            length = 0
            width = 0
        else: 
            tooBig = False
        
    # output the dimensions of the rectanlge as an svg file
    f = open("rectangle.svg","w")
    f.write('<?xml version = "1.0" encoding = "UTF-8" ?> \n')
    f.write('<svg xmlns="http://www.w3.org/2000/svg" version = "1.1"> \n')
    f.write(f'<rect x = "10" y = "10" width = "{width*inchToPix}" height = "{length*inchToPix}" stroke = "black" stroke-width = "2" fill = "none" /> \n')
    f.write('</svg>')
    f.close()

main()

