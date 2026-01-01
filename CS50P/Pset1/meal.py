
def convert(time):
    hours,minutes=time.split(':')
    f=float(hours)
    s=int(minutes)/60
    a=s+f
    return a
def main():
    r=convert(input("What time is it?"))
    if 7<=r<=8:
        print("breakfast time")
    if 12<=r<=13:
        print("lunch time")
    if 18<=r<=19:
        print("dinner time")


def convert(time):
    hours,minutes=time.split(':')
    f=float(hours)
    s=int(minutes)/60
    a=s+f
    return a
if __name__ == "__main__":
    main()



