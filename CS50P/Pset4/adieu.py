import inflect
p=inflect.engine()


list=[]
while True:
    try:
       s=input("Name:")
       i=list.append(s)
    except EOFError:
        print()
        break

final=p.join(list)
print("Adieu, adieu, to",final)
