e=input("camelCase: ")
s=""
d=len(e)
for x in range(d):
    if e[x].isupper():
        s+='_'+e[x].lower()
    else:
        s+=e[x]


print("snake_case: ",s)
