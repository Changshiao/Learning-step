Amount_Due=50

while(Amount_Due>0):
    print("Amount Due:",Amount_Due)
    Insert_coin=int(input("Insert Coin: "))
    if Insert_coin in [5,10,25]:
        Amount_Due-=Insert_coin

print("Change Owed:",abs(Amount_Due))

