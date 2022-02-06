# -*- coding: utf-8 -*-

# constants
MAX_WIDTH = 24.0 #verify this is the maximum width of the acrylic
MAX_HEIGHT = 18.0 #verify this is the maximum height of the acrylic
INCH_TO_PIX_CONV = 96 # one pixel = 1/96 inch
FONT_SIZE_CONV = 72 # size 1 pt font = 1/72 inch

# intro statements
print("--------------------------------------------------------------------------")
print("--------------------------------------------------------------------------")
print("This program helps you create a user-defined, customizable box.")
print('The box will be laser cut from acrylic (nominally 1/4" thick).')
print(f'The box cannot exceed dimensions which require more material than {MAX_HEIGHT}" X {MAX_WIDTH}".')
print("--------------------------------------------------------------------------")

# funciton to accept inputs from user
def userInput(thickness, width, length, height):
    
    #constants
    MAX_WIDTH = 24.0 #verify this is the maximum width of the acrylic
    MAX_HEIGHT = 18.0 #verify this is the maximum height of the acrylic
    MAX_THICKNESS = 0.5 # arbitraty maximum thickness

    # while loop placeholders
    tooBig = True # placeholder for initial while loop -> assume box too big until otherwise
    partitionInput = ""
    lidInput = ""
    
    # intial box value settings
    partition = False
    lid = False
    numPartitions = 0 

    # get user input for box values
    while tooBig == True or thickness <= 0 or width <= 0 or length <= 0 or height <= 0:

        # get user input for thickness
        while thickness <= 0 or thickness > MAX_THICKNESS:
            thickness = float(input('Enter a thickness (in) for the box walls: '))
            if thickness <= 0:
                print("Invalid thickness! Only positive values accepted.")
            if thickness > MAX_THICKNESS:
                print('Invalid thickness! That is very thick!')
                print(f'Let''s try something less than or equal to {MAX_THICKNESS}".')
        
        # get user input for width
        # NEED TO THINK ABOUT HOW WE ERROR CHECK FOR TOO LARGE
        # i'm thinking error checking will be later...
        while width <= 0:  
            width = float(input('Enter a width (in) for the box: '))
            if width <= 0:
                print("Invalid width! Only positive values accepted.")
            # if width > :
            #     print(f'Invalid width! Must be less than or equal to {}" or we run out of material.')

        # get user input for length
        # NEED TO THINK ABOUT HOW WE ERROR CHECK FOR TOO LARGE
        # i'm thinking error checking will be later...
        while length <= 0:
            length = float(input('Enter a length (in) for your box: '))
            if length <= 0:
                print("Invalid length! Only positive values accepted.")
            # if length > :
            #     print(f'Invalid length! Must be less than or equal to {}" or we run out of material.')

        # get user input for height
        # NEED TO THINK ABOUT HOW WE ERROR CHECK FOR TOO LARGE
        # i'm thinking error checking will be later...
        while height <= 0:
            height = float(input('Enter a height (in) for the rectangle: '))
            if height <= 0:
                print("Invalid height! Only positive values accepted.")
            # if height > :
            #     print(f'Invalid height!Must be less than or equal to {}" or we run out of material.')
        
        # set reference dimensions
        if width > length and width > height:
            longestDim = width
            if length > height or length == height:
                mediumDim = length
                shortestDim = height
            else:
                mediumDim = height
                shortestDim = length
        
        if length > width and length > height:
            longestDim = length
            if width > height or width == height:
                mediumDim = width
                shortestDim = height
            else: 
                mediumDim = height
                shortestDim = width

        if height > width and height > length:
            longestDim = height
            if width > length or width == length:
                mediumDim = width
                shortestDim = length
            else:
                mediumDim = length
                shortestDim = width

        # # as of 2/5/22, i have not fixed the issue with this loop -YL
        # while (partitionInput != "Y" or partitionInput != "N"):
        #     partitionInput = input("Would you like a partition for the box? Please Enter (Y/N):  ")
        #     if partitionInput == "Y":
        #         #partition = True
        #         while numPartitions < 0 or numPartitions > 2:
        #             numPartitions = input("You can have 1 or 2 partitions. Please enter how many: ")
        #     else:
        #         #partition = False
        #         numPartitions = 0

        # # as of 2/5/22, i have not fixed the issue with this loop -YL
        # while (lidInput != "Y" or lidInput != "N"):
        #     lidInput = input("Would you like a lid for the box? Please Enter (Y/N):  ")
        #     if lidInput == "Y":
        #         lid = True
        #     else:
        #         lid = False
            
        # OTHER USER INPUT OPTIONS? 
        # -Num. of dovetails? automatic? 
        # -initials? 
        # pattern? pick a size/ automatic? 
            
        # ERROR CHECK REFERENCE DIMS new function to error check? 
        ## need to check if longestDim x however many cuts (depending on if longest is w,l,h, lid/no-lid, partition(s)/no-partition(s)) exceeds the length/width of the acrylic... 
        ## also need to check rest of dims and remaining acrylic space... 

        # if :
        #     tooBig = True
        # else: 
        #     tooBig = False

        # before error checking, assuming that dims are good so tooBig = False
        tooBig = False
    return thickness, width, length, height, longestDim, mediumDim, shortestDim, numPartitions, lidInput

def main():
    
    # initialize thickness, length, width and height of the box to be zero
    thickness = 0.0
    width = 0.0
    length = 0.0
    height = 0.0

    # reference dimensions for SVG output
    longestDim = 0.0
    mediumDim = 0.0
    shortestDim = 0.0

    boxValues = userInput(thickness, width, length, height)
    # we can get rid of indivudual variables and just use the boxValues tuple... Whichever is easier
    thickness = boxValues[0]
    width = boxValues[1]
    length = boxValues[2]
    height = boxValues[3]
    longestDim = boxValues[4]
    mediumDim = boxValues[5]
    shortestDim = boxValues[6]
    numPartitions = boxValues[7]
    lid = boxValues[8]
    # printing to check
    print(f'thickness: {thickness}')
    print(f'width: {width}')
    print(f'length: {length}')
    print(f'height: {height}')
    print(f'longest: {longestDim}')
    print(f'medium: {mediumDim}')
    print(f'shortest: {shortestDim}')
    print(f'number of partitions: {numPartitions}')
    print(f'lid: {lid}')


main()
