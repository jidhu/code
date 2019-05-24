omoney=float(input("O hai! How much change is owed?\n"))
money=omoney-int(omoney)
money=round(money,2)

count=0

def cashier(count,money,types_of_coins):
    while(money>=types_of_coins):
        count+=1
        money-=types_of_coins
        money=round(money,2)
    return count,money

count,money=cashier(count,money,.25)
count,money=cashier(count,money,.10)
count,money=cashier(count,money,.05)
count,money=cashier(count,money,.01)

print(count)