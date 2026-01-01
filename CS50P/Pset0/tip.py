def dollars_to_float(d):
    f=d.lstrip('$')
    s=float(f)

    return s


def percent_to_float(p):
    t=p.rstrip('%')
    o=int(t)/100
    x=float(o)

    return x


def main():
    dollars = dollars_to_float(input("How much was the meal?:"))
    percent = percent_to_float(input("What percentage would you like to tip?:"))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")
main()






