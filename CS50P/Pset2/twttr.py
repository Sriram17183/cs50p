def main():
    e=input("Enter the word:")
    print(shorten(e))

def shorten(e):
    vowels=['A','E','I','O','U','a','e','i','o','u']
    p=""
    for i in e:
        if i in vowels:
            print("",end="")
        else:
            p=p+i

    return p
if __name__="__main__":
    main()

