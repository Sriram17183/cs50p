print("Amount Due:",50)
amountdue=50
coins=[5,10,25]
while amountdue>0:
    coin=int(input("Insert coin:"))
    if coin in coins:
        amountdue-=coin
        if amountdue>0:
            print(f"Amount Due: {amountdue}")
    else:
        amountdue=50
        print(f"Amount Due: {amountdue}")
print(f"Change Owed: {abs(amountdue)}")

