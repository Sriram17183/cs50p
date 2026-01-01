import random
while True:
    try:
        i=int(input("Level:"))
        if i > 0:
            break
    except:
        pass


r = random.randint(1,i)

while True:
    try:
        a = int(input("Guess:"))
        if a != 0:
            if 0 < a < r:
                print("Too small!")
            elif a > r:
                print("Too large!")
            elif a==r:
                print("Just Right!")
                break
    except:
        pass
