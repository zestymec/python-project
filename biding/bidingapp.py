from art import logo
import os

print(logo)


def findhighestvalue(database):
    winner = ""
    highestvalue = 0
    for bidder in database:
        bidamount = database[bidder]
        if bidamount > highestvalue:
            highestvalue = bidamount
            winner = bidder

    print(f"so the winner is {winner} bidammount is {bidamount}")


database = {}

continuebidings = True

while continuebidings:
    name = input("what is your name ?")
    bidprice = int(input("what is your bid price $"))
    database[name] = bidprice
    shouldcontinue = input("is there is any other who want to bid \n").lower()
    if shouldcontinue == "no":
        continuebidings = False
        findhighestvalue(database)
    elif shouldcontinue == "yes":
        os.system("cls" if os.name == "nt" else "clear")
        continuebidings = True
        
