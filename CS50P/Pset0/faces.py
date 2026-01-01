a=input("Enter any:")
if (":)") in a and (":(") in a:
    d=a.replace(":)","🙂").replace(":(","🙁")
    print(d)
elif (":)") in a:
    a=a.replace(":)","🙂")
    print(a)
elif (":(") in a:
    a=a.replace(":(","🙁")
    print(a)

