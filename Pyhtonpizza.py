print("Welcome to pYthon Pizza Deliverires")
size = input("What sixe do You like ? S M L")
pepperoni = input("do You want pepproni ? Y N ")
extra_cheese = input("Do You want extra cheese ? Y or N")
BIll = 0
if size == "S":
    BIll = 15
elif size == "M":
    BIll = 20
else:
    BIll = 25
if pepperoni == "Y" and size == "S":
    BIll += 2
elif pepperoni == "Y" and size == "M":
    BIll += 3
if extra_cheese == "Y":
    BIll += 1
print(f"now your bill price is ${BIll}")
