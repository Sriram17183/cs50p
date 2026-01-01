import sys
from PIL import Image, ImageOps

if len(sys.argv) <= 2:
    sys.exit("Too few command line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command line arguments")
if not (sys.argv[1].endswith('.png')==sys.argv[2].endswith('.png')):
    sys.exit("Input and Output have different extensions")
if  not (sys.argv[1].endswith('.jpg')==sys.argv[2].endswith('.jpg')) or not (sys.argv[1].endswith('.jpeg')==sys.argv[2].endswith('.jpeg')):
     sys.exit("Input and Output have different extensions")

inputfile= sys.argv[1]
outputfile = sys.argv[2]
try:
    with Image.open(inputfile) as base:
        with Image.open("shirt.png") as tshirt:
            tshirt = ImageOps.fit(tshirt, (600, 600))
            base= ImageOps.fit(base, (600, 600))
            base.paste(tshirt, (0, 0),tshirt)
            base.save(outputfile)
except FileNotFoundError:
    sys.exit("File does not exist")



