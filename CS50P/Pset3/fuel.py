
def main():
    d=input("Fraction:")
    data=convert(d)
    percent=gauge(data)
    print(percent)


def convert(s):
    try:
        x,y=s.split('/')
        x=int(x)
        y=int(y)
        k=round(x/y,3)
        l=int(k*(100))
        return l
    except ValueError:
        raise
    except ZeroDivisionError:
        raise


def gauge(g):
    if g>=99:
        return "F"
    elif g<=1:
        return "E"
    else:
        return f"{g}%"


if __name__=="__main__":
    main()


