#bunch of cards
cards=[]
def enter():
    while (len(cards)<14):
        choice=input("Enter the value want to be added?\n y/n\n> ")
        if choice == 'Y' or choice == 'y':
            i=input("Enter a card?\n> ")
            cards.append(i)
        else:
            print("No room for anymore cards")
            break

def display():
    list.sort(cards)
    for i in cards:
        print(cards[i])

def pop(x):
    cards.pop(x)

def insert(x,y):
    cards.insert(x,y)

def append(x):
    cards.append(x)
    list.sort(cards)

def search(x):
    for i in cards:
        if x==i:
            choice=input("You want to remove that card?\ty/n\n> ")
            if choice == 'Y' or choice == 'y':
                pop(ord(cards[x]))
print=('''welcome to the go cash game. Enter the cards you have''')

choice=input("")
enter()
