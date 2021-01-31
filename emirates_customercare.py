def bd():
    name = input("whats your name")
    age = input("whats your age")
    height = input("whats your height")
    weight = input("whats your weight")

def bag():
    FROM = input("where are you travelling from")
    TO = input("where are you travelling to")
    weight = int(input("What is the weight of the bag"))
    price = weight * 50
    print(price)

while True:
    emirates = int(input("Hi this is Sneha speaking, what problem are you facing ? \n booking flights press 1 \n baggage press 2 \n covid test press 3 :"))
    if emirates == 1:
       bd()
    elif emirates == 2:
       bag()
    elif emirates == 3:
       bd()





