
def kerf(f,spacingParam,shift):

    INCH_TO_PIX_CONV = 96
    xStartNW = 75+shift
    yStartNW = 75
    horizontalDim = 3
    verticalDim = 4
    thickness = .125

    ## CONSTANTS
    shiftForScrews = 25
    polylineLength = 5
    oscillator = 2 ## TO GET OFFSETS
    #spacingParam = 10 ## CAN CHANGE - SHIFTS VERTICAL DISTANCE
    spacingBetweenCurves = 20
    lengthOfCurve = 10

    f.write(f'<rect x = "{xStartNW - thickness*INCH_TO_PIX_CONV}" y = "{yStartNW-thickness*INCH_TO_PIX_CONV}" width = "{(horizontalDim + 2*thickness)*INCH_TO_PIX_CONV}" height = "{(verticalDim + 2*thickness)*INCH_TO_PIX_CONV}" style="fill:none;stroke:black;stroke:2"/>\n')

    totalLengthKerf = (horizontalDim + 2*thickness)*INCH_TO_PIX_CONV

    distanceToFill = totalLengthKerf - (spacingBetweenCurves - polylineLength*2 - lengthOfCurve)

    howManyCols = int(distanceToFill/spacingBetweenCurves)

    distanceToFillWithLines = distanceToFill - howManyCols*spacingBetweenCurves

    lengthOfStartAndEndLines = distanceToFillWithLines/2

    xKerfStart = xStartNW - thickness*INCH_TO_PIX_CONV + polylineLength
    yKerfStart = yStartNW - thickness*INCH_TO_PIX_CONV + shiftForScrews

    for i in range(howManyCols): ##the width
        oscillator = oscillator*(-1)

        for j in range(24): ## THE LENGTH

            if i == 0:
                f.write(f'<polyline points = "{xStartNW - thickness*INCH_TO_PIX_CONV},{yStartNW + shiftForScrews + j*spacingParam + oscillator - thickness*INCH_TO_PIX_CONV} {xStartNW + lengthOfStartAndEndLines - thickness*INCH_TO_PIX_CONV},{yStartNW + j*spacingParam + oscillator + shiftForScrews - thickness*INCH_TO_PIX_CONV}" fill = "none" stroke = "black" /> \n')

            f.write(f'<polyline points = "{xStartNW + i*spacingBetweenCurves + lengthOfStartAndEndLines - thickness*INCH_TO_PIX_CONV + (spacingBetweenCurves - lengthOfCurve - 2*polylineLength)},{yStartNW + shiftForScrews + j*spacingParam + oscillator - thickness*INCH_TO_PIX_CONV} {xStartNW + i*spacingBetweenCurves + polylineLength - thickness*INCH_TO_PIX_CONV + lengthOfStartAndEndLines + (spacingBetweenCurves - lengthOfCurve - 2*polylineLength)},{yStartNW + j*spacingParam + oscillator + shiftForScrews - thickness*INCH_TO_PIX_CONV}" fill = "none" stroke = "black" /> \n')
            f.write(f'<path d = "M {xStartNW + i*spacingBetweenCurves + polylineLength - thickness*INCH_TO_PIX_CONV + lengthOfStartAndEndLines + (spacingBetweenCurves - lengthOfCurve - 2*polylineLength)} {yKerfStart + j*spacingParam + oscillator} C {xStartNW + i*spacingBetweenCurves + polylineLength - thickness*INCH_TO_PIX_CONV + lengthOfStartAndEndLines + (spacingBetweenCurves - lengthOfCurve - 2*polylineLength)} {yKerfStart + 10 + j*spacingParam + oscillator}, {xStartNW + i*spacingBetweenCurves + polylineLength - thickness*INCH_TO_PIX_CONV + lengthOfStartAndEndLines + (spacingBetweenCurves - lengthOfCurve - 2*polylineLength) + lengthOfCurve} {yKerfStart + 10 + j*spacingParam + oscillator}, {xStartNW + i*spacingBetweenCurves + polylineLength - thickness*INCH_TO_PIX_CONV + lengthOfStartAndEndLines + (spacingBetweenCurves - lengthOfCurve - 2*polylineLength) + lengthOfCurve} {yKerfStart + j*spacingParam + oscillator}" stroke = "black" fill = "transparent"/>\n')
            f.write(f'<polyline points = "{xStartNW + i*spacingBetweenCurves + polylineLength - thickness*INCH_TO_PIX_CONV + lengthOfStartAndEndLines + (spacingBetweenCurves - lengthOfCurve - 2*polylineLength) + lengthOfCurve} {yKerfStart + j*spacingParam + oscillator} {xStartNW + i*spacingBetweenCurves + polylineLength - thickness*INCH_TO_PIX_CONV + lengthOfStartAndEndLines + (spacingBetweenCurves - lengthOfCurve - 2*polylineLength) + lengthOfCurve + polylineLength},{yKerfStart + j*spacingParam + oscillator}" fill = "none" stroke = "black" /> \n')

            if i == (howManyCols -1):
                f.write(f'<polyline points = "{xStartNW + i*spacingBetweenCurves + polylineLength - thickness*INCH_TO_PIX_CONV + lengthOfStartAndEndLines + (spacingBetweenCurves - lengthOfCurve - 2*polylineLength)*2 + lengthOfCurve + polylineLength} {yKerfStart + j*spacingParam + oscillator} {xStartNW - thickness*INCH_TO_PIX_CONV + (horizontalDim + 2*thickness)*INCH_TO_PIX_CONV},{yKerfStart + j*spacingParam + oscillator}" fill = "none" stroke = "black" /> \n')
    
    text = "spacing param ="
    f.write(f'<text x = "{xStartNW + (horizontalDim*INCH_TO_PIX_CONV)/2}" y = "{yStartNW + (verticalDim*INCH_TO_PIX_CONV)/1.25}" dominant-baseline= "central" text-anchor= "middle" font-size = "30px" fill = "blue">' + str(spacingParam) + ' </text> \n')

    
    
def main():

    shift = 4
    f = open("kerf5.svg",'w')

    f.write('<?xml version = "1.0" encoding = "UTF-8" ?> \n')
    f.write('<svg xmlns="http://www.w3.org/2000/svg" version = "1.1"> \n')
    #kerf(f,10,0)
    #kerf(f,9,shift*96)
    # kerf(f,8,shift*0*96)
    # kerf(f,7.5, shift*1*96)
    # kerf(f,7, shift*0*96)
    # kerf(f,6.5, shift*1*96)
    kerf(f,6, shift*0*96)
    kerf(f,5.5, shift*1*96)
    # kerf(f,5, shift*6*96)
    # kerf(f,4.5, shift*7*96)
    f.write('</svg>')
    f.close()


main()