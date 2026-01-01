from pyfiglet import Figlet
import sys
import random
fig=Figlet()
u=["-f","--font"]
fonts=fig.getFonts()

if len(sys.argv)==1:
    new=random.choice(fonts)

elif len (sys.argv)==3 and sys.argv[2] in fonts and sys.argv[1] in u:
    new=sys.argv[2]
else:
    sys.exit("Inavlid usage")

t=input("Input: ")
fig.setFont(font=new)
print(fig.renderText(t))
