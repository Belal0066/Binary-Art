from PIL import Image # u need to install pillow first
from math import floor

chars = ' 10'
charsArray = list(chars)
charsLength = len(charsArray)
ratio = charsLength / 256

def getChar(inputInt):
    return charsArray[floor(inputInt * ratio)]

image = Image.open("C:\\Users\\PC\\Desktop\\eastman.png")  #u r photo path
text = open('text.txt', 'w') #the output text file

scaleFactor = 0.35 
oneCharWidth = 10
oneCharHeight = 15

width, height = image.size
image = image.resize((int(scaleFactor*width),
int(scaleFactor*height*(oneCharWidth/oneCharHeight))),
Image.NEAREST)
width, height = image.size
pic = image.load()

for h in range(height):
    for w in range(width):
        r, g, b = pic[w, h]
        x = int(r/3 + g/3 + b/3)
        pic[w, h] = (x, x, x) 
        text.write(getChar(x))

    text.write('\n')
