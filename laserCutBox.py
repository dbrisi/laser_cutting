# -*- coding: utf-8 -*-

# ACTION ITEMS
# 1. input for pattern - in userAddOnInput() -DJD
# 2. input for text on top - in userAddOnInput(), call new fct -YLL                 DONE
# 3. input for text on front - in userAddOnInput(), call new fct -YLL               DONE
# 4. # error checking dimensions - in userDimInput() -DJD 
# 5. start svg generation - new "master" fct, calls other svg generations -YLL
# 6. fractal pattern - new function (called by master svg function) -DJD
# 7. text on top for SVG - new function, called by master svg fct -YLL
# 8. text on bottom for SVG - new function, called by master svg fct -YLL
# 9. one (same) function for each dimension input, called by userDimInput() -YLL    DONE



# constants
MAX_WIDTH = 24.0 #verify this is the maximum width of the acrylic
MAX_HEIGHT = 18.0 #verify this is the maximum height of the acrylic
INCH_TO_PIX_CONV = 96 # one pixel = 1/96 inch --> MAYBE CHANGE?
FONT_SIZE_CONV = 72 # size 1 pt font = 1/72 inch

# intro statements
print("--------------------------------------------------------------------------")
print("--------------------------------------------------------------------------")
print("This program helps you create a user-defined, customizable box.")
print('The box will be laser cut from acrylic (nominally 1/4" thick).')
print(f'The box cannot exceed dimensions which require more material than {MAX_WIDTH}" X {MAX_HEIGHT}".')
print("--------------------------------------------------------------------------")

#######################################################
## FUNCTION TO ACCEPT USER INPUTS FOR BOX DIMENSIONS ##
#######################################################
def userDimInput(thickness, width, length, height):
    
    #constants
    MAX_WIDTH = 24.0 #verify this is the maximum width of the acrylic
    MAX_HEIGHT = 18.0 #verify this is the maximum height of the acrylic
    MAX_THICKNESS = 0.5 # arbitraty maximum thickness

    # while loop placeholder
    tooBig = True # placeholder for initial while loop -> assume box too big until otherwise

    # get user input for box values
    while tooBig == True or thickness <= 0 or width <= 0 or length <= 0 or height <= 0:

        # get user input for thickness
        while thickness <= 0 or thickness > MAX_THICKNESS:
            thickness = float(input('Enter a thickness (in) for the box walls (nominally .25"): '))
            if thickness <= 0:
                print("Invalid thickness! Only positive values accepted.")
            if thickness > MAX_THICKNESS:
                print('Invalid thickness! That is very thick!')
                print(f'How about something less than or equal to {MAX_THICKNESS}"?')
        
        # get user input for width
        width = userSingleDim("width",width,thickness)
        
        # get user input for length
        length = userSingleDim("length",length,thickness)

        # get user input for height
        height = userSingleDim("height",height,thickness)

        # set reference dimensions -> new function? 
        if width > length and width > height:
            longestDim = width
            longestDimInd = "w"
            if length > height or length == height:
                mediumDim = length
                mediumDimInd = "l"
                shortestDim = height
                shortestDimInd = "h"
            else:
                mediumDim = height
                mediumDimInd = "h"
                shortestDim = length
                shortestDimInd = 'l'
        
        if length > width and length > height:
            longestDim = length
            longestDimInd = 'l'
            if width > height or width == height:
                mediumDim = width
                mediumDimInd = 'w'
                shortestDim = height
                shortestDimInd = 'h'
            else: 
                mediumDim = height
                mediumDimInd = 'h'
                shortestDim = width
                shortestDimInd = 'w'

        if height > width and height > length:
            longestDim = height
            longestDimInd = 'h'
            if width > length or width == length:
                mediumDim = width
                mediumDimInd = 'w'
                shortestDim = length
                shortestDimInd = 'l'
            else:
                mediumDim = length
                mediumDimInd = 'l'
                shortestDim = width
                shortestDimInd = 'w'

    # ERROR CHECK REFERENCE DIMS new function to error check? 
        ## need to check if longestDim x however many cuts (depending on if longest is w,l,h, lid/no-lid, partition(s)/no-partition(s)) exceeds the length/width of the acrylic... 
        ## also need to check rest of dims and remaining acrylic space... 

        # if :
        #     tooBig = True
        # else: 
        #     tooBig = False


        # before error checking, assuming that dims are good so tooBig = False
        tooBig = False

    return thickness, width, length, height, longestDim, mediumDim, shortestDim, longestDimInd, mediumDimInd, shortestDimInd

##########################################################
## FUNCTION TO ACCEPT USER INPUTS FOR BOX ADD-ON VALUES ##
##########################################################
def userAddOnInputs(length):
    # while loop placeholders
    partitionInput = ""
    lidInput = ""
    topTextInput = ""
    frontTextInput = ""
    topText = ""

    # intial box value settings
    partition = False
    lid = False
    topTextYesNo = False # maybe this is not necessary (just check if text is "" or has something)
    frontTextYesNo = False # maybe this is not necessary (just check if text is "" or has something)
    #numPartitions = 0 
    partitionLocation = 0

    # user input for partition option and location
    # maybe consider giving the user the option to choose the orientation (legnth/width-wise) of the partition
    while (partitionInput != "Y" and partitionInput != "N"):
        partitionInput = input("Would you like a partition for the box? Please Enter (Y/N): ").upper()
        if partitionInput == "Y":
            partition = True
            while partitionLocation <= 0 or partitionLocation > length:
                partitionLocation = float(input("Enter the location (in) of the partition: ")) #maybe clarify length/width later
                if partitionLocation < 0:
                    print("Invalid length. Please enter a positive value")
                if partitionLocation > length:
                    print("Invalid length. Please enter a value which is less than the length.")
        else:
            partition = False

    # user input for lid option
    while (lidInput != "Y" and lidInput != "N"):
        lidInput = input("Would you like a lid for the box? Please Enter (Y/N):  ").upper()
        if lidInput == "Y":
            lid = True
        else:
            lid = False

    # user input for text option and content
    while (topTextInput != "Y" and topTextInput != "N"):
        topTextValues = textInput("top")
        topTextInput = topTextValues[0]
        topTextYesNo = topTextValues[1]
        topText = topTextValues[2] 
    
    # user input for text option and content
    while (frontTextInput != "Y" and frontTextInput != "N"):
        frontTextValues = textInput("front")
        frontTextInput = frontTextValues[0]
        frontTextYesNo = frontTextValues[1]
        frontText = frontTextValues[2] 

    #Simple case: Width and Length along width of acrylic (24"), Height along height of acrylic (18"

    # OTHER USER INPUT OPTIONS? 
    # -Num. of dovetails? automatic? --> NO for now, start with fixed size of dovetails
    # -ask for text message on front and/or top --> YES
    # pattern? pick a size/ automatic? --> YES, give options for one (or both) sides, one for now

    return partition, partitionLocation, lid, topTextYesNo, topText, frontTextYesNo, frontText
    
############################################
## FUNCTION TO ACCEPT USER INPUT FOR TEXT ##
############################################
def textInput(location):
    textInput = input(f"Would you like text on the {location} of your box? Please enter Y/N: ").upper()
    if textInput == "Y":
        print('OK, text will be autosized to fit the dimensions of the box.') # in the meantime... 
        YesNo = True
        text = input("Please enter the text: ")
    else: 
        YesNo = False
        text = "" # necessary?
    
    return textInput, YesNo, text

##########################################################
## FUNCTION TO ACCEPT USER INPUT FOR A SINGLE DIMENSION ##
##########################################################
def userSingleDim(dimension, dimensionValue, thickness):
    while dimensionValue <= 0 or dimensionValue > 24 - 2*thickness:
        dimensionValue = float(input(f'Enter a {dimension} (in) for the box: '))
        if dimensionValue <= 0:
            print(f"Invalid {dimension}! Only positive values accepted.")
        if dimensionValue > 24 - 2*thickness:
            print(f'Invalid {dimension}! Maximum dimension of the available material is only 24". Please try again.')
            
    return dimensionValue

###################
## MAIN FUNCTION ##
###################
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

    boxDims = userDimInput(thickness, width, length, height)
     # we can get rid of indivudual variables and just use the boxDims tuple... Whichever is easier
    thickness = boxDims[0]
    width = boxDims[1]
    length = boxDims[2]
    height = boxDims[3]
    longestDim = boxDims[4]
    mediumDim = boxDims[5]
    shortestDim = boxDims[6]
    longestDimInd = boxDims[7]
    mediumDimInd = boxDims[8]
    shortestDimInd = boxDims[9]

    boxValues = userAddOnInputs(length)
    # we can get rid of indivudual variables and just use the boxValues tuple... Whichever is easier
    partition = boxValues[0]
    partitionLength = boxValues[1]
    lid = boxValues[2]
    topTextYesNo = boxValues[3]
    topText = boxValues[4]
    frontTextYesNo = boxValues[5]
    frontText = boxValues[6]

    # printing to check
    print('---------------------')
    print('Results for testing:')
    print('---------------------')
    print("Dimensions:")
    print(f'thickness: \t\t{thickness}')
    print(f'width:  \t\t{width}')
    print(f'length: \t\t{length}')
    print(f'height: \t\t{height}')
    print(f'longest: \t\t{longestDim}')
    print(f'medium: \t\t{mediumDim}')
    print(f'shortest: \t\t{shortestDim}')
    print(f'Longest: \t\t{longestDimInd}')
    print(f'Medium: \t\t{mediumDimInd}')
    print(f'Shortest: \t\t{shortestDimInd}')
    print('---------------------')
    print('Add-ons:')
    print(f'partition: \t\t{partition}')
    print(f'location of partition: \t{partitionLength}')
    print(f'lid: \t\t\t{lid}')
    print(f'top: \t\t\t{topTextYesNo}')
    print(f'top text content: \t{topText}')
    print(f'front text: \t\t{frontTextYesNo}')
    print(f'front text content: \t{frontText}')

main()

