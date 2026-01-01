from validator_collection import checkers

s=input("What's your email address?")


e=checkers.is_email(s)
if e==True:
    print("Valid")
else:
    print("Invalid")
 
