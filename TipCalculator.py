print("Welcome to our tip calculator! ")

totallbill = float(input("What was the totall bill ?"))

tippercent = float(input("How much percent tip would you like to give 10 , 12 or 15 ? "))

totall_people = float(input("How many people to split the bill ? "))

tip_value = (totallbill * tippercent) / 100


totallbillbecomes = totallbill + tip_value

share_value = round(totallbillbecomes / totall_people)

print(f"tip value is {tip_value}Rs")

print(f"{share_value}Rs is your share")
