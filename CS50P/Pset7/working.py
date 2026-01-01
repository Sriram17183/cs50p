import re
import sys

def main():
    print(convert(input("Hours:")))

def start_(f):
    f = str(f).strip()
    if len(f) == 7:
        hour = f[0]
        minute = f[2:4]
        if int(minute) == 60:
            raise ValueError
        if f[5:]=="AM" and int(hour)==12:
            hour=f'00'
        elif f[5:] == "AM":
            hour = f"0{hour}"
        else:
            if int(hour) == 12:
                hour = int(hour)
            else:
                hour = int(hour) + 12

    elif len(f) == 5:
        hour = f[0:2]
        minute = '00'
        if f[3:]=="AM" and int(hour)==12:
            hour=f'00'
        elif f[3:] == "AM":
            hour = f"0{hour}"
        else:
            if int(hour) == 12:
                hour = int(hour)
            else:
                hour = int(hour) + 12

    elif len(f) == 4:
        hour = f[0]
        minute = '00'
        if f[2:]=="AM" and int(hour)==12:
            hour=f'00'
        elif f[2:] == "AM":
            hour = f"0{hour}"
        else:
            if int(hour) == 12:
                hour = int(hour)
            else:
                hour = int(hour) + 12


    elif len(f) == 8:
        hour = f[0:2]
        minute = f[3:5]
        if int(minute) == 60:
            raise ValueError
        if f[6:]=="AM" and int(hour)==12:
            hour=f'00'
        elif f[6:] == "AM":
            hour = f"0{hour}"
        else:
            if int(hour) == 12:
                hour = int(hour)
            else:
                hour = int(hour) + 12
    else:
        raise ValueError

    return f"{int(hour):02}:{minute}"


def end_(d):
    d = str(d).strip()
    if len(d) == 7:
        hour = d[0]
        minute = d[2:4]
        if int(minute) == 60:
            raise ValueError
        if d[5:]=="AM" and int(hour)==12:
            hour=f'00'
        elif d[5:] == "AM":
            hour = f"0{hour}"
        else:
            if int(hour) == 12:
                hour = int(hour)
            else:
                hour = int(hour) + 12

    elif len(d) == 8:
        hour = d[0:2]
        minute = d[3:5]
        if int(minute) == 60:
            raise ValueError
        if d[6:]=="AM" and int(hour)==12:
            hour=f'00'
        elif d[6:] == "AM":
            hour = f"0{hour}"
        else:
            if int(hour) == 12:
                hour = int(hour)
            else:
                hour = int(hour) + 12
    elif len(d) == 4:
        hour = d[0]
        minute = '00'
        if d[2:]=="AM" and int(hour)==12:
            hour=f'00'
        elif d[2:] == "AM":
            hour = f"0{hour}"
        else:
            if int(hour) == 12:
                hour = int(hour)
            else:
                hour = int(hour) + 12

    elif len(d) == 5:
        hour = d[0:2]
        minute = '00'
        if d[3:]=="AM" and int(hour)==12:
            hour=f'00'
        elif d[3:] == "AM":
            hour = f"0{hour}"
        else:
            if int(hour) == 12:
                hour = int(hour)
            else:
                hour = int(hour) + 12
    else:
        raise ValueError

    return f"{int(hour):02}:{minute}"


def convert(s):
    if time := re.search(r"(\d{1,2}(?::\d{2})?\s*[AP]M)\s*(?:to)\s*(\d{1,2}(?::\d{2})?\s*[AP]M)", s, re.IGNORECASE):
        start = time.group(1)
        end = time.group(2)
        starter = start_(start)
        ender = end_(end)
        return f"{starter} to {ender}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
