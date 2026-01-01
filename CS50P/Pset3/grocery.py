d={}
while True:
    try:
        u=input("")
        u=u.upper()
        if u in d:
            d[u]+=1
        else:
            d[u]=1
    except EOFError:
        for t in sorted(d):
            print(d[t],t)
        break


