

f = open("Testtext.svg","w")


FONT_SIZE_CONV = 72
INCH_TO_PIX_CONV = 96

def textSVG(f, text, xStart, yStart, horizontalDim = 4, verticalDim = 3):
    # if len(text) < 7:
    #     fontSize = FONT_SIZE_CONV*(5/len(text))
    # else:
    fontSize = FONT_SIZE_CONV*(2*horizontalDim/len(text))
    f.write('<?xml version = "1.0" encoding = "UTF-8" ?> \n')
    f.write('<svg xmlns="http://www.w3.org/2000/svg" version = "1.1"> \n')
    f.write(f'<rect x = "{xStart}" y = "{yStart}" width = "{horizontalDim*INCH_TO_PIX_CONV}" height = "{verticalDim*INCH_TO_PIX_CONV}" fill = "none" stroke = "black" stroke-width = "4"/> \n')
    f.write(f'<text x = "{xStart + (horizontalDim*INCH_TO_PIX_CONV)/2}" y = "{yStart + (verticalDim*INCH_TO_PIX_CONV)/2}" dominant-baseline= "central" text-anchor= "middle" font = "courier" font-size = "{fontSize}px" fill = "red">' + text + ' </text> \n')
    #f.write(f'<text x = "{xStart + (horizontalDim*INCH_TO_PIX_CONV)/2}" y = "{yStart + (verticalDim*INCH_TO_PIX_CONV)/2}" dominant-baseline= "central" text-anchor= "middle" font-size = "30px" fill = "red">' + text + ' </text> \n')
    f.write('</svg>')

def main():
    text = input("Enter text:")
    width = int(input("width: "))
    height = int(input("height: "))
    textSVG(f,text,75,75, width, height)

main()