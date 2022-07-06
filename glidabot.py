import facebook
import PIL
from PIL import Image, ImageDraw, ImageFont
import textwrap
import random
import codecs
import unicodedata

#Read a random line from any text file
def readRandomLine(file):
    lines = codecs.open(file, 'r', encoding='utf-8').readlines()
    return random.choice(lines)

#Final string initialize
finalPara = ""

#Decides how many ingridients the ice cream will contain
items = random.randint(1, 5)

#Adding ingridients to the string
for i in range(0, items):
    val = readRandomLine('ingridients.txt')
    while(len(val) <= 0 or val in finalPara):
        val = readRandomLine('ingridients.txt')
    finalPara += val

#Add a holder
val = readRandomLine('holders.txt')
while(len(val) <= 0):
        val = readRandomLine('holders.txt')
finalPara += val

#Add a random ending
chance = random.randint(0, 3)
if chance == 1:
    finalPara += "\n"
    finalPara += readRandomLine('endings.txt')

#Bypass Facebook spam protection
img = Image.new('RGBA', (540, 1), color = "White")
img.save('out.png')

#Debug
print(finalPara)

#Post to Facebook
facebook = facebook.GraphAPI("(Enter your Facebook token here)")
response = facebook.put_photo(image=open('out.png', 'rb'), message=finalPara)
postId = response['post_id']
print("Photo posted with id: " + postId)
