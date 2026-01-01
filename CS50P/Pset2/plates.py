def is_valid(s):
        if s[0:2].isalpha() and 2<=len(s)<=6:
            for char in s:
                 if char.isdigit() and char !='0':
                    index=s.index(char)
                    if s[index:].isdigit():
                        return True
                    else:
                        return False
                 if char=='0':
                    return False
                 else:
                    continue
            return True
        else:
            return False
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")




if __name__=="__main__":
    main()



