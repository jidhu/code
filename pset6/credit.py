#american express 15 start with 34 or 37
#master card 16 starts with 51, 52, 53, 54, 55
#visa 13 and 16 starts with 4

card=input("Number: ")
card=[int(i) for i in str(card)]
products_sum=0

if(len(card)==15 and card[0]==3):
    type_of_card='AMEX'
elif(len(card)==16 and card[0]==5):
    type_of_card='MASTERCARD'
elif((len(card)==13 or len(card)==16) and card[0]==4):
    type_of_card='VISA'
else:
    type_of_card="INVALID"

for i in range(1,len(card),2):
    products_sum+=card[i]*2
    if(products_sum>=10):
        products_sum-=10
        products_sum+=1

for i in range(0,len(card),2):
    products_sum+=card[i]

#if(products_sum%10!=0):
    #type_of_card="INVALID"

print(type_of_card)