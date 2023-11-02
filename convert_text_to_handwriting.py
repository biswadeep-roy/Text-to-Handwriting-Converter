from PIL import Image
import sys


if len(sys.argv) > 1:
    input_filename = sys.argv[1]
else:
    input_filename = "test.txt"  

try:
    with open(input_filename, "r") as txt:
        text = txt.read().replace("\n", "")
except FileNotFoundError:
    print("Could not find the file:", input_filename)
    sys.exit(1)

BG = Image.open("myfont/bg.png")
sheet_width = BG.width
gap, ht = 0, 0

for char in text:
    try:
        char_code = ord(char)
        char_image = Image.open("font/{}.png".format(char_code))
        BG.paste(char_image, (gap, ht))
        size = char_image.width
        height = char_image.height
        gap += size

        if sheet_width < gap or len(char) * 115 > (sheet_width - gap):
            gap, ht = 0, ht + 140

    except FileNotFoundError:
        print(f"Could not find an image for character '{char}' (code {char_code})")

print("Total gap:", gap)
print("Sheet width:", sheet_width)
BG.show()
