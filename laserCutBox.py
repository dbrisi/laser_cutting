#########################################################################################
#########################################################################################
## A python program to take user input and output an SVG file that can laser cut a box ##
#########################################################################################
#########################################################################################

# imports
import math

# constants
MAX_WIDTH = 18 #verify this is the maximum width of the acrylic
MAX_HEIGHT = 12 #verify this is the maximum height of the acrylic
MAX_THICKNESS = 0.5 # arbitraty maximum thickness
INCH_TO_PIX_CONV = 96*(2/5) # one inch = 96 pixels, 2:5 scale
MM_TO_PIX_CONV = 3.7795275591*(2/5) # one mm = 3.78... pixels, , 2:5 scale
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

    # while loop placeholder
    tooBig = True # placeholder for initial while loop -> assume box too big until otherwise

    # get user input for box values
    while tooBig == True or thickness <= 0 or width <= 0 or length <= 0 or height <= 0:

        # get user input for thickness
        while thickness <= 0 or thickness > MAX_THICKNESS:
            isFloat = True
            try:
                thickness = float(input('Enter a thickness (in) for the box walls (nominally .118"): '))
            except ValueError:
                print('Invalid thickness! Only numerical values are accepted.')
                isFloat = False
                thickness = 0.0
    
            if isFloat == True:
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

        # error checking dimensions, .5 accounts for piece separation
        if (2*width + 2*length + 8*thickness + .5) > MAX_WIDTH or (height + length + 4* thickness + .25) > MAX_HEIGHT:
            tooBig = True
            print('Your entered dimensions exceed the allowable material to cut.')
            print(f'The maximum allowable cutting area is {MAX_WIDTH}" X {MAX_HEIGHT}"')
            print(f'{MAX_WIDTH}" includes twice the width, twice the length, eight times thickness and piece seperation.')
            print(f'{MAX_HEIGHT}" includes the length, the height, four times thickness and piece seperation.')
            print('Please try again.')
            print("--------------------------------------------------------------------------")
            
            thickness, width, length, height = 0,0,0,0
        else:
            tooBig = False

    return thickness, width, length, height

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
    fractalInput = ""
    fractalSideChoiceInput = ""

    # intial box value settings
    partition = False
    lid = False
    topTextYesNo = False 
    frontTextYesNo = False 
    partitionLocation = 0
    fractal = False

    # user input for partition option and location
    while (partitionInput != "Y" and partitionInput != "N"):
        partitionInput = input("Would you like a partition for the box? Please Enter (Y/N): ").upper()
        if partitionInput == "Y":
            partition = True
            while partitionLocation <= 0 or partitionLocation > length:
                partitionLocation = float(input("Enter the location (in) of the partition, measured from the front of the box: ")) 
                if partitionLocation < 0:
                    print("Invalid length. Please enter a positive value")
                if partitionLocation > length:
                    print("Invalid length. Please enter a value which is less than the length.")
        if partitionInput != "Y" and partitionInput != "N":
            print('You did not enter a valid response. Please try again.')
        else:
            partition = False

    # user input for lid option
    while (lidInput != "Y" and lidInput != "N"):
        lidInput = input("Would you like a lid for the box? Please Enter (Y/N):  ").upper()
        if lidInput == "Y":
            lid = True
        else:
            lid = False
        if lidInput != "Y" and lidInput != "N":
            print('You did not enter a valid response. Please try again.')

    # user input for text option and content
    if lid == True:
        while (topTextInput != "Y" and topTextInput != "N"):
            topTextValues = textInput("top")
            topTextInput = topTextValues[0]
            topTextYesNo = topTextValues[1]
            topText = topTextValues[2]
            if topTextInput != "Y" and topTextInput != "N":
                print('You did not enter a valid response. Please try again.')

    # user input for text option and content
    while (frontTextInput != "Y" and frontTextInput != "N"):
        frontTextValues = textInput("front")
        frontTextInput = frontTextValues[0]
        frontTextYesNo = frontTextValues[1]
        frontText = frontTextValues[2]
        if frontTextInput != "Y" and frontTextInput != "N":
            print('You did not enter a valid response. Please try again.')

    # user input for the fractal
    while (fractalInput != "Y" and fractalInput != "N"):
        fractalInput = input("Would you like a fractal pattern on one side of the box? Please Enter (Y/N): ").upper()
        if fractalInput == "Y":
            fractal = True
            while (fractalSideChoiceInput != "SIDE" and fractalSideChoiceInput != "BOTTOM"):
                fractalSideChoiceInput = input("Enter the location of the fractal - Side or Bottom: ").upper()
                if fractalSideChoiceInput != "SIDE" and fractalSideChoiceInput != "BOTTOM":
                    print('You did not enter a valid response. Please try again.')
        else:
            fractal = False
        if fractalInput != "Y" and fractalInput != "N":
            print('You did not enter a valid response. Please try again.')

    return partition, partitionLocation, lid, topTextYesNo, topText, frontTextYesNo, frontText, fractal, fractalSideChoiceInput

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
    while dimensionValue <= 0 or dimensionValue > 18 - 2*thickness:
        isFloat = True

        try: 
           dimensionValue = float(input(f'Enter a {dimension} (in) for the box walls: '))
        except ValueError:
            print(f'Invalid {dimension}! Only positive, numerical values are accepted.')
            isFloat = False
            dimensionValue = 0.0

        if isFloat == True:
            dimensionValue = int(dimensionValue)
            if dimensionValue <= 0:
                print(f"Invalid {dimension}! Only positive values accepted.")
            if dimensionValue > 18 - 2*thickness - .5:
                print(f'Invalid {dimension}! Maximum dimension of the available material is only 18". \nPlease try again. Account for thickness and piece separation.')
    
    return dimensionValue

#########################################
## FUNCTION TO GENERATE FRACTAL IN SVG ##
#########################################
def fractalGenerator(f,fractalSide, x, y, width, length, height):

    xStart = x
    yStart = y

    fracSpaceParam = .75

    if fractalSide == "SIDE":
        minDistance = int(min(height, width))
    else:
        minDistance = int(min(width, length))

    f.write(f'<polyline points = "{xStart},{yStart} {xStart + fracSpaceParam*math.cos(59*math.pi/180)},{yStart + fracSpaceParam*math.sin(59*math.pi/180)}" fill = "none" stroke = "red" /> \n')

    for i in range(22*minDistance):
        f.write(f'<polyline points = "{xStart + fracSpaceParam*math.cos(59*i*math.pi/180)*i},{yStart + fracSpaceParam*math.sin(59*i*math.pi/180)*i} {xStart + fracSpaceParam*math.cos(59*(i+1)*math.pi/180)*(i+1)},{yStart + fracSpaceParam*math.sin(59*(i+1)*math.pi/180)*(i+1)}" fill = "none" stroke = "red" /> \n')

######################################
## FUNCTION TO GENERATE TEXT IN SVG ##
######################################
def textSVG(f, text, xStart, yStart, horizontalDim, verticalDim, position):
    if verticalDim < horizontalDim:
        fontSize = FONT_SIZE_CONV*(1/5)*verticalDim
    else:
        fontSize = FONT_SIZE_CONV*(1/10)*horizontalDim
    if position == "TOP":
        fontSize = FONT_SIZE_CONV*(1/20)*verticalDim
        f.write(f'<text x = "{xStart + (horizontalDim*INCH_TO_PIX_CONV)/2}" y = "{yStart + (verticalDim*INCH_TO_PIX_CONV)/1.05}" dominant-baseline= "central" text-anchor= "middle" font-size = "14px" fill = "blue">' + text + ' </text> \n')
    else:
        #f.write(f'<text x = "{xStart + (horizontalDim*INCH_TO_PIX_CONV)/2}" y = "{yStart + (verticalDim*INCH_TO_PIX_CONV)/2}" dominant-baseline= "central" text-anchor= "middle" font-size = "{fontSize}px" fill = "red">' + text + ' </text> \n')
        f.write(f'<text x = "{xStart + (horizontalDim*INCH_TO_PIX_CONV)/2}" y = "{yStart + (verticalDim*INCH_TO_PIX_CONV)/2}" dominant-baseline= "central" text-anchor= "middle" font-size = "30px" fill = "blue">' + text + ' </text> \n')

#######################################
## FUNCTION TO GENERATE BASES IN SVG ##
#######################################
def baseSVG(f, position, thickness, horizontalDim, verticalDim, X_START, Y_START, partition = False, partitionLocation = None, lid = False):

    #INCH_TO_PIX_CONV = 96

    # AS OF NOW KEEP AS DOVETAIL AS .5" AND USE ONLY FULL INTEGER DIMENSIONS
    doveTailLength = .5 #in
    partitionDoveTailLength = .5 # in
    partitionDoveTailDistance = .25 # in

    # SCREW and NUT DIMENSIONS
    screwLength = 10 - 3 #mm with NO added clearance --> Added the "-3" to account for an issue later, easier to fix this way (in the meantime)
    screwDiam = 2 + 0.5 #mm with added clearance
    squareNutSide = 5#mm ## with NO added clearance
    squareNutThickness = 1.5#mm with NO added clearance
    nutDistanceFromEdge = 4 #mm
    distanceAfterNut = 3 #mm
    shiftDown = (verticalDim-1)*INCH_TO_PIX_CONV
    shiftRight = (horizontalDim-1)*INCH_TO_PIX_CONV

    xStartNW = X_START
    yStartNW = Y_START
    xStartNE = xStartNW + horizontalDim*INCH_TO_PIX_CONV
    yStartNE = yStartNW
    xStartSE = xStartNE
    yStartSE = yStartNE + verticalDim*INCH_TO_PIX_CONV
    xStartSW = xStartSE - horizontalDim*INCH_TO_PIX_CONV
    yStartSW = yStartSE

    if position == "TOP":

        ## CONSTANTS
        shiftForScrews = .3*INCH_TO_PIX_CONV
        #polylineLength = 1
        #oscillator = .8 ## TO GET OFFSETS --- delete
        spacingParam = 1/8*INCH_TO_PIX_CONV ## CAN CHANGE - SHIFTS VERTICAL DISTANCE
        #spacingBetweenCurves = 4
        spacingBetweenLines1 = 1/16*INCH_TO_PIX_CONV
        spacingBetweenLines2 = 1/16*INCH_TO_PIX_CONV
        #lengthOfCurve = 3
        lineLength1 = .7*INCH_TO_PIX_CONV
        lineLength2 = .7*INCH_TO_PIX_CONV

        xOffset = (lineLength1)
        #curvatureAdj = 1

        # outline of the lid
        x1,y1 = xStartNW - thickness*INCH_TO_PIX_CONV, yStartNW-thickness*INCH_TO_PIX_CONV
        x2,y2 = x1 + (horizontalDim+2*thickness)*INCH_TO_PIX_CONV*(1/3), y1
        x3,y3 = x2, y2 + thickness*INCH_TO_PIX_CONV
        x4,y4 = x3 + (horizontalDim+2*thickness)*INCH_TO_PIX_CONV*(1/3), y3
        x5,y5 = x4, y1
        x6,y6 = x1 + (horizontalDim + 2*thickness)*INCH_TO_PIX_CONV, y1
        x7,y7 = x6, y1 + (verticalDim + 2*thickness)*INCH_TO_PIX_CONV
        x8,y8 = x1,y7
        x9,y9 = x1,y1

        f.write(f'<polyline points = "{x1},{y1} {x2},{y2} {x3},{y3} {x4},{y4} {x5},{y5} {x6},{y6} {x7},{y7} {x8},{y8} {x9},{y9}" style="fill:none;stroke:black;stroke:2"/>\n')

        # holes for the lid
        xHole1,yHole1  = xStartNW + horizontalDim*INCH_TO_PIX_CONV/6, yStartNW - thickness*INCH_TO_PIX_CONV/2 + screwDiam*MM_TO_PIX_CONV/2
        xHole2, yHole2 = xStartNW + horizontalDim*INCH_TO_PIX_CONV*(5/6), yHole1
        f.write(f'<circle cx = "{xHole1}" cy = "{yHole1}" r = "{screwDiam*MM_TO_PIX_CONV/2}" style="fill:none;stroke:black;stroke:1"/>\n')
        f.write(f'<circle cx = "{xHole2}" cy = "{yHole2}" r = "{screwDiam*MM_TO_PIX_CONV/2}" style="fill:none;stroke:black;stroke:1"/>\n')

        # kerf pattern
        totalLengthKerfLine1 = (horizontalDim + 2*thickness)*INCH_TO_PIX_CONV
        #print(totalLengthKerfLine1)
        totalLengthKerfLine2 = totalLengthKerfLine1 - xOffset
        #distanceToFill = totalLengthKerf - (lineLength - spacingBetweenLines - lengthOfCurve)
        howManyColsLine1 = int(totalLengthKerfLine1/(lineLength1 + 2*spacingBetweenLines1))
        #print(howManyColsLine1)
        howManyColsLine2 = int(totalLengthKerfLine2/(lineLength2 + 2*spacingBetweenLines2))
        distanceToFillWithBookends1 = totalLengthKerfLine1 - (lineLength1 + 1*spacingBetweenLines1)*howManyColsLine1 - spacingBetweenLines1
        distanceToFillWithBookends2 = totalLengthKerfLine2 - (lineLength2 + 1*spacingBetweenLines2)*howManyColsLine2 - spacingBetweenLines2
        lengthOfStartAndEndLine1 = distanceToFillWithBookends1/2
        lengthOfStartAndEndLine2 = distanceToFillWithBookends2/2
        #xKerfStart = xStartNW - thickness*INCH_TO_PIX_CONV + polylineLength
        #yKerfStart = yStartNW - thickness*INCH_TO_PIX_CONV + shiftForScrews

        for i in range(howManyColsLine1): ##the width
            #oscillator = oscillator*(-1)

            kerfLengthIterations = int(verticalDim*(28/4))#length = 4, range = 28
            for j in range(kerfLengthIterations): ## THE LENGTH
                BegLineStartY = yStartNW + shiftForScrews + j*spacingParam - thickness*INCH_TO_PIX_CONV
                BegLineStartY2 = (yStartNW + shiftForScrews + j*spacingParam - thickness*INCH_TO_PIX_CONV + yStartNW + shiftForScrews + (j+1)*spacingParam - thickness*INCH_TO_PIX_CONV)/2


                if i == 0:
                    BegLineStartX = xStartNW - thickness*INCH_TO_PIX_CONV
                    BegLineFinishX = xStartNW + lengthOfStartAndEndLine1 - thickness*INCH_TO_PIX_CONV

                    f.write(f'<polyline points = "{BegLineStartX},{BegLineStartY} {BegLineFinishX},{BegLineStartY}" fill = "none" stroke = "black" /> \n')

                f.write(f'<polyline points = "{BegLineFinishX + (i+1)*spacingBetweenLines1 + lineLength1*i},{BegLineStartY} {BegLineFinishX + (i+1)*spacingBetweenLines1 + lineLength1*(i+1)},{BegLineStartY}" fill = "none" stroke = "black" /> \n')
                #f.write(f'<polyline points = "{(BegLineStartX + BegLineFinishX + (i+1)*spacingBetweenLines1 + lineLength1*i)/2},{BegLineStartY2} {(BegLineStartX + BegLineFinishX + (i+1)*spacingBetweenLines1 + lineLength1*i)/2 + (i+1)*spacingBetweenLines1 + lineLength1*(i+1)},{BegLineStartY2}" fill = "none" stroke = "black" /> \n')

                if i == (howManyColsLine1 -1):
                    f.write(f'<polyline points = "{BegLineFinishX + (i+1)*spacingBetweenLines1 + spacingBetweenLines1 + lineLength1*(i+1)} {BegLineStartY} {BegLineFinishX + (i+1)*spacingBetweenLines1 + spacingBetweenLines1 + lineLength1*(i+1) + lengthOfStartAndEndLine1},{BegLineStartY}" fill = "none" stroke = "black" /> \n')
                    f.write(f'<polyline points = "{BegLineStartX + spacingBetweenLines1},{BegLineStartY2} {totalLengthKerfLine1 + BegLineStartX - spacingBetweenLines1},{BegLineStartY2}" fill = "none" stroke = "black" /> \n')

    # if not the lid/top
    else:
        # horizontal side 1 (NW to NE) --> Top side of SVG base
        f.write('<polyline points="')
        x1,y1 = xStartNW,  yStartNW
        if position == "BOTTOM":
            x2,y2 = x1, y1 -thickness*INCH_TO_PIX_CONV
            x3,y3 = x2 + doveTailLength*INCH_TO_PIX_CONV, y2
            x4,y4 = x3, yStartNW
            x5,y5 = x4 + doveTailLength*INCH_TO_PIX_CONV, yStartNW
            for i in range(int(horizontalDim)):
                increment = i*INCH_TO_PIX_CONV
                f.write(f'{x1+increment},{y1} {x2+increment},{y2} {x3+increment},{y3} {x4+increment},{y4} {x5+increment},{y5} ')
        elif position == "BACK" and lid == True:
            x1,y1 = xStartNW - thickness*INCH_TO_PIX_CONV, yStartNW
            x2,y2 = x1 + (horizontalDim+2*thickness)*INCH_TO_PIX_CONV*(1/3), y1
            x3,y3 = x2, y2 - thickness*INCH_TO_PIX_CONV
            x4,y4 = x3 + (horizontalDim+2*thickness)*INCH_TO_PIX_CONV*(1/3), y3
            x5,y5 = x4, y1
            x6,y6 = x1 + (horizontalDim + 2*thickness)*INCH_TO_PIX_CONV, y1
            f.write(f'{x1},{y1} {x2},{y2} {x3},{y3} {x4},{y4} {x5},{y5} {x6},{y6}')
        else:
            f.write(f'{xStartNW},{yStartNW} {xStartNE},{yStartNE} ')
        f.write('" style="fill:none;stroke:black;stroke:2"/>\n')

        # slots for screws and nuts for lid connection
        if position == "BACK" and lid == True:
            shiftForLid = horizontalDim*INCH_TO_PIX_CONV*(2/3)

            x1,y1  = xStartNW + horizontalDim*INCH_TO_PIX_CONV/6 - screwDiam*MM_TO_PIX_CONV/2, yStartNW
            x2,y2  = x1, y1 + (screwLength-squareNutSide - distanceAfterNut)*MM_TO_PIX_CONV + thickness*INCH_TO_PIX_CONV
            x3,y3  = x2 - (squareNutSide - screwDiam)*MM_TO_PIX_CONV/2, y2
            x4,y4  = x3, y3 + squareNutThickness*MM_TO_PIX_CONV
            x5,y5  = x2, y4
            x6,y6  = x5, y5 + distanceAfterNut*MM_TO_PIX_CONV
            x7,y7  = x6 + screwDiam*MM_TO_PIX_CONV, y6
            x8,y8  = x7, y5
            x9,y9  = x8 + (squareNutSide - screwDiam)*MM_TO_PIX_CONV/2, y8
            x10,y10  = x9, y3
            x11,y11  = x8, y3
            x12,y12  = x11, y1

            f.write(f'<line x1 = "{x1}" y1 = "{y1}" x2 = "{x12}" y2 = "{y12}" style="fill:none;stroke:white;stroke:2"/>\n')
            f.write(f'<line x1 = "{x1 + shiftForLid}" y1 = "{y1}" x2 = "{x12 + shiftForLid}" y2 = "{y12}" style="fill:none;stroke:white;stroke:2"/>\n')
            f.write(f'<polyline points = "{x1},{y1} {x2},{y2} {x3},{y3} {x4},{y4} {x5},{y5} {x6},{y6} {x7},{y7} {x8},{y8} {x9},{y9} {x10},{y10} {x11},{y11} {x12},{y12}" style="fill:none;stroke:black;stroke:2"/>\n')
            f.write(f'<polyline points = "{x1 + shiftForLid},{y1} {x2 + shiftForLid},{y2} {x3 + shiftForLid},{y3} {x4 + shiftForLid},{y4} {x5 + shiftForLid},{y5} {x6 + shiftForLid},{y6} {x7 + shiftForLid},{y7} {x8 + shiftForLid},{y8} {x9 + shiftForLid},{y9} {x10 + shiftForLid},{y10} {x11 + shiftForLid},{y11} {x12 + shiftForLid},{y12}" style="fill:none;stroke:black;stroke:2"/>\n')
            f.write(f'<line x1 = "{xStartNW - thickness*INCH_TO_PIX_CONV}" y1 = "{yStartNW}" x2 = "{xStartNW}" y2 = "{yStartNW}" style="fill:none;stroke:white;stroke:2"/>\n')

        # holes for screws and dovetails on bottom
        if position == "BOTTOM":
            xHole1,yHole1  = xStartNW + doveTailLength*INCH_TO_PIX_CONV/2, yStartNW - thickness*INCH_TO_PIX_CONV/2 + screwDiam*MM_TO_PIX_CONV/2
            xHole2, yHole2 = xHole1 +shiftRight, yHole1
            f.write(f'<circle cx = "{xHole1}" cy = "{yHole1}" r = "{screwDiam*MM_TO_PIX_CONV/2}" style="fill:none;stroke:black;stroke:1"/>\n')
            f.write(f'<circle cx = "{xHole2}" cy = "{yHole2}" r = "{screwDiam*MM_TO_PIX_CONV/2}" style="fill:none;stroke:black;stroke:1"/>\n')

        # vertical side 1 (NE to SE) --> Right side of SVG base
        x1,y1 = xStartNE,  yStartNE
        f.write('<polyline points="')

        # only two dovetails for partition
        if position == "PARTITION":
            x1, y1 = xStartNE, yStartNE
            x2, y2 = x1, yStartNE + partitionDoveTailDistance*INCH_TO_PIX_CONV
            x3, y3 = xStartNE + thickness*INCH_TO_PIX_CONV, y2
            x4, y4 = x3, y3 + doveTailLength*INCH_TO_PIX_CONV
            x5, y5 = x1, y4
            x6, y6 = x5, yStartNE + (verticalDim - partitionDoveTailDistance - partitionDoveTailLength)*INCH_TO_PIX_CONV
            x7, y7 = x5 + thickness*INCH_TO_PIX_CONV, y6
            x8, y8 = x7, y7 + doveTailLength*INCH_TO_PIX_CONV
            x9, y9 = x1, y8
            x10, y10 = x1, yStartNE + verticalDim*INCH_TO_PIX_CONV

            f.write(f'{x1},{y1} {x2},{y2} {x3},{y3} {x4},{y4} {x5},{y5} {x6},{y6} {x7},{y7} {x8},{y8} {x9},{y9} {x10},{y10}')

        # every other piece has normal dovetail pattern
        else:
            x2,y2 = x1 + thickness*INCH_TO_PIX_CONV, y1
            x3,y3 = x2, y2 + doveTailLength*INCH_TO_PIX_CONV
            x4,y4 = xStartNE, y3
            x5,y5 = xStartNE, y4 + doveTailLength*INCH_TO_PIX_CONV
            for i in range(int(verticalDim)):
                increment = i*INCH_TO_PIX_CONV
                f.write(f'{x1},{y1+increment} {x2},{y2+increment} {x3},{y3+increment} {x4},{y4+increment} {x5},{y5+increment} ')
        f.write('" style="fill:none;stroke:black;stroke:2"/>\n')

        # slots for screws and nuts - side connections
        if (position == "FRONT" or position == "BACK" or position == "LEFT" or position == "RIGHT"):
            x1,y1  = xStartNE, yStartNE + 1.5*doveTailLength*INCH_TO_PIX_CONV - screwDiam*MM_TO_PIX_CONV/2
            x2,y2  = x1 - (screwLength-squareNutSide - distanceAfterNut)*MM_TO_PIX_CONV - thickness*INCH_TO_PIX_CONV, y1
            x3,y3  = x2, y2 - (squareNutSide - screwDiam)*MM_TO_PIX_CONV/2
            x4,y4  = x3 - squareNutThickness*MM_TO_PIX_CONV, y3
            x5,y5  = x4, y2
            x6,y6  = x5 - distanceAfterNut*MM_TO_PIX_CONV, y5
            x7,y7  = x6, y6 + screwDiam*MM_TO_PIX_CONV
            x8,y8  = x5,y7
            x9,y9  = x4, y8 + (squareNutSide - screwDiam)*MM_TO_PIX_CONV/2
            x10,y10  = x3, y9
            x11,y11  = x10, y8
            x12,y12  = x1, y11

            f.write(f'<line x1 = "{x1}" y1 = "{y1}" x2 = "{x12}" y2 = "{y12}" style="fill:none;stroke:white;stroke:2"/>\n')
            f.write(f'<line x1 = "{x1}" y1 = "{y1 + shiftDown}" x2 = "{x12}" y2 = "{y12 + shiftDown}" style="fill:none;stroke:white;stroke:2"/>\n')
            f.write(f'<polyline points = "{x1},{y1} {x2},{y2} {x3},{y3} {x4},{y4} {x5},{y5} {x6},{y6} {x7},{y7} {x8},{y8} {x9},{y9} {x10},{y10} {x11},{y11} {x12},{y12}" style="fill:none;stroke:black;stroke:2"/>\n')
            f.write(f'<polyline points = "{x1},{y1 + shiftDown} {x2},{y2 + shiftDown} {x3},{y3 + shiftDown} {x4},{y4 + shiftDown} {x5},{y5 + shiftDown} {x6},{y6 + shiftDown} {x7},{y7 + shiftDown} {x8},{y8 + shiftDown} {x9},{y9 + shiftDown} {x10},{y10 + shiftDown} {x11},{y11 + shiftDown} {x12},{y12 + shiftDown}" style="fill:none;stroke:black;stroke:2"/>\n')

        # horizontal side 2 (SE to SW) --> Bottom side of SVG base
        x1,y1 = xStartSE,  yStartSE
        f.write('<polyline points="')

        # flat for partition
        if position == "PARTITION":
            f.write(f'{xStartSE},{yStartSE} {xStartSW},{yStartSW} ')

        # normal pattern for every other side
        else:
            x2,y2 = x1, y1 + thickness*INCH_TO_PIX_CONV
            x3,y3 = x2 - doveTailLength*INCH_TO_PIX_CONV, y2
            x4,y4 = x3, yStartSE
            x5,y5 = x4 - doveTailLength*INCH_TO_PIX_CONV, yStartSE
            for i in range(int(horizontalDim)):
                increment = i*INCH_TO_PIX_CONV
                f.write(f'{x1-increment},{y1} {x2-increment},{y2} {x3-increment},{y3} {x4-increment},{y4} {x5-increment},{y5} ')

        f.write('" style="fill:none;stroke:black;stroke:2"/>\n')

        # holes for screws - bottom connection (only bottom piece)
        if position == "BOTTOM":
            xHole1,yHole1  = xStartSW + 1.5*doveTailLength*INCH_TO_PIX_CONV, yStartSW + thickness*INCH_TO_PIX_CONV/2 - screwDiam*MM_TO_PIX_CONV/2
            xHole2, yHole2 = xHole1 +shiftRight, yHole1
            f.write(f'<circle cx = "{xHole1}" cy = "{yHole1}" r = "{screwDiam*MM_TO_PIX_CONV/2}" style="fill:none;stroke:black;stroke:1"/>\n')
            f.write(f'<circle cx = "{xHole2}" cy = "{yHole2}" r = "{screwDiam*MM_TO_PIX_CONV/2}" style="fill:none;stroke:black;stroke:1"/>\n')

        # slots for screws and nuts - bottom connection (front and back pieces)
        if position == "FRONT" or position == "BACK":
            x1,y1  = xStartSW + doveTailLength*INCH_TO_PIX_CONV/2 - screwDiam*MM_TO_PIX_CONV/2, yStartSW
            x2,y2  = x1, y1 - (screwLength-squareNutSide - distanceAfterNut)*MM_TO_PIX_CONV - thickness*INCH_TO_PIX_CONV
            x3,y3  = x2 - (squareNutSide - screwDiam)*MM_TO_PIX_CONV/2, y2
            x4,y4  = x3, y3 - squareNutThickness*MM_TO_PIX_CONV
            x5,y5  = x2, y4
            x6,y6  = x5, y5 - distanceAfterNut*MM_TO_PIX_CONV
            x7,y7  = x6 + screwDiam*MM_TO_PIX_CONV, y6
            x8,y8  = x7, y5
            x9,y9  = x8+ (squareNutSide - screwDiam)*MM_TO_PIX_CONV/2, y8
            x10,y10  = x9, y3
            x11,y11  = x8, y3
            x12,y12  = x11, y1

            f.write(f'<line x1 = "{x1}" y1 = "{y1}" x2 = "{x12}" y2 = "{y12}" style="fill:none;stroke:white;stroke:2"/>\n')
            f.write(f'<line x1 = "{x1 + shiftRight}" y1 = "{y1}" x2 = "{x12 + shiftRight}" y2 = "{y12}" style="fill:none;stroke:white;stroke:2"/>\n')
            f.write(f'<polyline points = "{x1},{y1} {x2},{y2} {x3},{y3} {x4},{y4} {x5},{y5} {x6},{y6} {x7},{y7} {x8},{y8} {x9},{y9} {x10},{y10} {x11},{y11} {x12},{y12}" style="fill:none;stroke:black;stroke:2"/>\n')
            f.write(f'<polyline points = "{x1 + shiftRight},{y1} {x2 + shiftRight},{y2} {x3 + shiftRight},{y3} {x4 + shiftRight},{y4} {x5 + shiftRight},{y5} {x6 + shiftRight},{y6} {x7 + shiftRight},{y7} {x8 + shiftRight},{y8} {x9 + shiftRight},{y9} {x10 + shiftRight},{y10} {x11 + shiftRight},{y11} {x12 + shiftRight},{y12}" style="fill:none;stroke:black;stroke:2"/>\n')

        # vertical side 2 (SW to NW) --> Left side of base SVG
        x1,y1 = xStartSW,  yStartSW
        f.write('<polyline points="')

        # less dovetails for partition
        if position == "PARTITION":
            x1, y1 = xStartNW, yStartNW
            x2, y2 = x1, yStartNW + partitionDoveTailDistance*INCH_TO_PIX_CONV
            x3, y3 = xStartNW - thickness*INCH_TO_PIX_CONV, y2
            x4, y4 = x3, y3 + doveTailLength*INCH_TO_PIX_CONV
            x5, y5 = x1, y4
            x6, y6 = x5, yStartNW + (verticalDim - partitionDoveTailDistance - partitionDoveTailLength)*INCH_TO_PIX_CONV
            x7, y7 = x5 - thickness*INCH_TO_PIX_CONV, y6
            x8, y8 = x7, y7 + doveTailLength*INCH_TO_PIX_CONV
            x9, y9 = x1, y8
            x10, y10 = x1, yStartNW + verticalDim*INCH_TO_PIX_CONV

            f.write(f'{x1},{y1} {x2},{y2} {x3},{y3} {x4},{y4} {x5},{y5} {x6},{y6} {x7},{y7} {x8},{y8} {x9},{y9} {x10},{y10}')

        # normal dovetail for every other piece
        else:
            x2,y2 = x1 - thickness*INCH_TO_PIX_CONV, y1
            x3,y3 = x2, y2 - doveTailLength*INCH_TO_PIX_CONV
            x4,y4 = xStartSW, y3
            x5,y5 = xStartSW, y4 - doveTailLength*INCH_TO_PIX_CONV
            for i in range(int(verticalDim)):
                increment = i*INCH_TO_PIX_CONV
                f.write(f'{x1},{y1-increment} {x2},{y2-increment} {x3},{y3-increment} {x4},{y4-increment} {x5},{y5-increment} ')

        f.write('" style="fill:none;stroke:black;stroke:2"/>\n')

        # holes for side connection
        if (position == "FRONT" or position == "BACK" or position == "LEFT" or position == "RIGHT"):
            xHole1,yHole1  = xStartNW - thickness*INCH_TO_PIX_CONV/2 + screwDiam*MM_TO_PIX_CONV/2, yStartNW + 1.5*doveTailLength*INCH_TO_PIX_CONV
            xHole2,yHole2 = xHole1, yHole1 + shiftDown
            f.write(f'<circle cx = "{xHole1}" cy = "{yHole1}" r = "{screwDiam*MM_TO_PIX_CONV/2}" style="fill:none;stroke:black;stroke:2"/>\n')
            f.write(f'<circle cx = "{xHole2}" cy = "{yHole2}" r = "{screwDiam*MM_TO_PIX_CONV/2}" style="fill:none;stroke:black;stroke:2"/>\n')

        # slots for partition
        if (position == "LEFT" and partition == True):
            f.write(f'<rect x = "{X_START + (partitionLocation*INCH_TO_PIX_CONV) - (thickness*INCH_TO_PIX_CONV)/2}" y = "{Y_START + (partitionDoveTailDistance*INCH_TO_PIX_CONV)}" width = "{thickness*INCH_TO_PIX_CONV}" height = "{partitionDoveTailLength*INCH_TO_PIX_CONV}" style="fill:none;stroke:black;strokeDim:3"/>\n')
            f.write(f'<rect x = "{X_START + (partitionLocation*INCH_TO_PIX_CONV) - (thickness*INCH_TO_PIX_CONV)/2}" y = "{Y_START + ((verticalDim - partitionDoveTailLength - partitionDoveTailDistance)*INCH_TO_PIX_CONV)}" width = "{thickness*INCH_TO_PIX_CONV}" height = "{partitionDoveTailLength*INCH_TO_PIX_CONV}" style="fill:none;stroke:black;strokeDim:3"/>\n')
        if (position == "RIGHT" and partition == True):
            f.write(f'<rect x = "{X_START + horizontalDim*INCH_TO_PIX_CONV - (partitionLocation*INCH_TO_PIX_CONV) - (thickness*INCH_TO_PIX_CONV)/2}" y = "{Y_START + (partitionDoveTailDistance*INCH_TO_PIX_CONV)}" width = "{thickness*INCH_TO_PIX_CONV}" height = "{partitionDoveTailLength*INCH_TO_PIX_CONV}" style="fill:none;stroke:black;strokeDim:3"/>\n')
            f.write(f'<rect x = "{X_START + horizontalDim*INCH_TO_PIX_CONV - (partitionLocation*INCH_TO_PIX_CONV) - (thickness*INCH_TO_PIX_CONV)/2}" y = "{Y_START + ((verticalDim - partitionDoveTailLength - partitionDoveTailDistance)*INCH_TO_PIX_CONV)}" width = "{thickness*INCH_TO_PIX_CONV}" height = "{partitionDoveTailLength*INCH_TO_PIX_CONV}" style="fill:none;stroke:black;strokeDim:3"/>\n')

##############################################################
## FUNCTION TO GENERATE MAIN SVG, CALLS OTHER SVG FUNCTIONS ##
##############################################################
def masterSVG(thickness, width, length, height, partition, partitionLocation, lid, topTextYesNo, topText, frontTextYesNo, frontText, fractal, fractalSideChoiceInput):

    # origin of SVG 
    xScale1, yScale1 = 25,20 #pixels
    xScale2,yScale2 = xScale1 + 1*INCH_TO_PIX_CONV, yScale1 #pixels
    X_START, Y_START = 25, 30 #pixels
    
    # seperation between pieces
    PIECE_SEPARATION = 5 #pixels

    # local origins of base pieces to be cut
    # row 1 of pieces
    xStartFront, yStartFront = X_START, Y_START
    xStartBack, yStartBack = xStartFront + (width + 2*thickness)*INCH_TO_PIX_CONV + PIECE_SEPARATION, Y_START
    xStartLeft, yStartLeft = xStartBack + (width + 2* thickness)*INCH_TO_PIX_CONV + PIECE_SEPARATION, Y_START
    xStartRight, yStartRight = xStartLeft + (length + 2* thickness)*INCH_TO_PIX_CONV + PIECE_SEPARATION, Y_START
    # row 2 of pieces
    xStartTop, yStartTop = X_START, Y_START + (height + 2*thickness)*INCH_TO_PIX_CONV + PIECE_SEPARATION
    xStartBottom, yStartBottom = xStartTop + (width + 2*thickness)*INCH_TO_PIX_CONV + PIECE_SEPARATION, Y_START + (height + 2*thickness)*INCH_TO_PIX_CONV + PIECE_SEPARATION
    xStartPartition, yStartPartition = xStartBottom + (width + 2*thickness)*INCH_TO_PIX_CONV + PIECE_SEPARATION, Y_START + (height + 2*thickness)*INCH_TO_PIX_CONV + PIECE_SEPARATION

    # create SVG file, will be saved in local repo/directory
    fileNameInput = input('Enter a file name (no extension): ')
    fileName = fileNameInput + ".svg"
    f = open(fileName,'w')

    # opening lines of SVG file
    f.write('<?xml version = "1.0" encoding = "UTF-8" ?> \n')
    f.write('<svg xmlns="http://www.w3.org/2000/svg" version = "1.1"> \n')

    # set and display scale of 1"
    f.write(f'<line x1="{xScale1}" y1="{yScale1}" x2="{xScale2}" y2 ="{yScale2}" style="stroke:red;stroke:4"/>\n')
    f.write(f'<text x = "{xScale2+10}" y = "{yScale2+5}" font-size = "12px" fill = "red"> = 1 inch (2:5 scale) </text> \n')
    #f.write(f'<text x = "{xScale2 + 30} y = "{yScale2+5} font-size = "20px" fill = "red"> RED = SCORE </text> \n')
    #f.write(f'<text x = "{xScale2 + spacingBetweenCurves} y = "{yScale2+5} font-size = "20px" fill = "black"> black = ENGRAVING </text> \n')

    # CALLING SVG generation functions

    # required SVG generation
    baseSVG(f,"FRONT",thickness,width,height,xStartFront,yStartFront)
    baseSVG(f,"BACK",thickness,width,height,xStartBack,yStartBack, partition, partitionLocation, lid)
    baseSVG(f,"LEFT",thickness,length,height,xStartLeft,yStartLeft,partition, partitionLocation)
    baseSVG(f,"RIGHT",thickness,length,height,xStartRight,yStartRight,partition, partitionLocation)
    baseSVG(f,"BOTTOM",thickness,width,length,xStartBottom,yStartBottom)

    # optional SVG generation
    if (partition == True):
        baseSVG(f,"PARTITION",thickness, width, height, xStartPartition, yStartPartition, partition, partitionLocation)

    if (lid == True):
        baseSVG(f,"TOP",thickness,width, length, xStartTop, yStartTop, partition, partitionLocation, lid)

    if fractal == True:
        if fractalSideChoiceInput == "SIDE":
            xFractal = xStartLeft + (length*INCH_TO_PIX_CONV)/2
            yFractal = yStartLeft + (height*INCH_TO_PIX_CONV)/2
        else:
            xFractal = xStartBottom + (width*INCH_TO_PIX_CONV)/2
            yFractal = yStartBottom + (length*INCH_TO_PIX_CONV)/2
        fractalGenerator(f,fractalSideChoiceInput,xFractal,yFractal, width, length, height)

    if (topTextYesNo == True):
        textSVG(f,topText,xStartTop,yStartTop,width,length, "TOP")

    if (frontTextYesNo == True):
        textSVG(f,frontText,xStartFront,yStartFront,width,height, "FRONT")

    #display box attributes below cut out pattern
    yAtt = yScale1 + (height+length + 4*thickness)*INCH_TO_PIX_CONV + 25
    xAtt1, xAtt2 = 20,200

    f.write(f'<text x = "{xScale1}" y = "{yAtt}" dy = "0">\n')
    # f.write(f'\t<tspan dy = ".6em"> BOX ATTRIBUTES < /tspan>\n')
    f.write(f'<tspan x = "{xAtt1}" dy = ".6em" >BOX ATTRIBUTES </tspan>\n')
    f.write(f'<tspan x = "{xAtt1}" dy = "1.2em" >thickness: </tspan>\n')
    f.write(f'<tspan x = "{xAtt1}" dy = "1.2em" >width: </tspan>\n')
    f.write(f'<tspan x = "{xAtt1}" dy = "1.2em" >length:  </tspan>\n')
    f.write(f'<tspan x = "{xAtt1}" dy = "1.2em" >height: </tspan>\n')
    f.write(f'<tspan x = "{xAtt1}" dy = "1.2em" >partition:  </tspan>\n')
    f.write(f'<tspan x = "{xAtt1}" dy = "1.2em" >partition location: </tspan>\n')
    f.write(f'<tspan x = "{xAtt1}" dy = "1.2em" >lid: </tspan>\n')
    f.write(f'<tspan x = "{xAtt1}" dy = "1.2em" >top text: </tspan>\n')
    f.write(f'<tspan x = "{xAtt1}" dy = "1.2em" >front text: </tspan>\n')
    f.write(f'<tspan x = "{xAtt1}" dy = "1.2em" >fractal: </tspan>\n')
    f.write(f'<tspan x = "{xAtt1}" dy = "1.2em" >fractal side/bottom: </tspan>\n')
    f.write(f'<tspan x = "{xAtt1}" dy = "1.2em" >front text string: </tspan>\n')
    f.write(f'<tspan x = "{xAtt1}" dy = "1.2em" >top text string: </tspan>\n')
    
    f.write('</text>')

    f.write(f'<text x = "{xAtt2}" y = "{yAtt}" dy = "0">\n')
    f.write(f'<tspan x = "{xAtt2}" dy = ".6em" > VALUES </tspan>\n')
    f.write(f'<tspan x = "{xAtt2}" dy = "1.2em" >' + str(thickness) +'</tspan>\n')
    f.write(f'<tspan x = "{xAtt2}" dy = "1.2em" >' + str(width) + '</tspan>\n')
    f.write(f'<tspan x = "{xAtt2}" dy = "1.2em" >' + str(length) + '</tspan>\n')
    f.write(f'<tspan x = "{xAtt2}" dy = "1.2em" >' + str(height) + '</tspan>\n')
    f.write(f'<tspan x = "{xAtt2}" dy = "1.2em" >' + str(partition) + '</tspan>\n')
    f.write(f'<tspan x = "{xAtt2}" dy = "1.2em" >' + str(partitionLocation) +'</tspan>\n')
    f.write(f'<tspan x = "{xAtt2}" dy = "1.2em" >' + str(lid)  + '</tspan>\n')
    f.write(f'<tspan x = "{xAtt2}" dy = "1.2em" >' + str(topTextYesNo) + '</tspan>\n')
    f.write(f'<tspan x = "{xAtt2}" dy = "1.2em" >' + str(frontTextYesNo) + '</tspan>\n')
    f.write(f'<tspan x = "{xAtt2}" dy = "1.2em" >' + str(fractal) + '</tspan>\n')
    f.write(f'<tspan x = "{xAtt2}" dy = "1.2em" >' + fractalSideChoiceInput.lower() + '</tspan>\n')
    f.write(f'<tspan x = "{xAtt2}" dy = "1.2em" >' + frontText + '</tspan>\n')
    f.write(f'<tspan x = "{xAtt2}" dy = "1.2em" >' + topText + '</tspan>\n')

    f.write('</text>')

    # closing line of SVG file
    f.write('</svg>')
    f.close()

###################
## MAIN FUNCTION ##
###################
def main():

    # initialize thickness, length, width and height of the box to be zero
    thickness = 0.0
    width = 0.0
    length = 0.0
    height = 0.0

    boxDims = userDimInput(thickness, width, length, height)

     # we can get rid of indivudual variables and just use the boxDims tuple... Whichever is easier
    thickness = boxDims[0]
    width = boxDims[1]
    length = boxDims[2]
    height = boxDims[3]

    boxValues = userAddOnInputs(length)
    # we can get rid of indivudual variables and just use the boxValues tuple... Whichever is easier
    partition = boxValues[0]
    partitionLocation = boxValues[1]
    lid = boxValues[2]
    topTextYesNo = boxValues[3]
    topText = boxValues[4]
    frontTextYesNo = boxValues[5]
    frontText = boxValues[6]
    fractal = boxValues[7]
    fractalSideChoiceInput = boxValues[8]

    # CALL SVG FUNCTIONS
    masterSVG(thickness,width,length,height,partition,partitionLocation,lid,topTextYesNo,topText,frontTextYesNo,frontText,fractal,fractalSideChoiceInput)

    # printing results to check
    print('---------------------')
    print('Results for testing:')
    print('---------------------')
    print("Dimensions:")
    print(f'thickness: \t\t{thickness}')
    print(f'width:  \t\t{width}')
    print(f'length: \t\t{length}')
    print(f'height: \t\t{height}')
    
    print('---------------------')
    print('Add-ons:')
    print(f'partition: \t\t{partition}')
    print(f'location of partition: \t{partitionLocation}')
    print(f'lid: \t\t\t{lid}')
    print(f'top: \t\t\t{topTextYesNo}')
    print(f'top text content: \t{topText}')
    print(f'front text: \t\t{frontTextYesNo}')
    print(f'front text content: \t{frontText}')
    print(f'fractal: \t\t{fractal}')
    print(f'fractal side: \t\t{fractalSideChoiceInput}')

main()
