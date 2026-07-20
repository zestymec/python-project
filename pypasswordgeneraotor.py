import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

chars = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']


print("Welcome to the PyPassword Generator!")
numberofletters = int((input("How many letter would you like in you password? \n")))
Symbols = int((input("How many symbols would you like ?\n")))
Numbers = int(input("How many numbers would you like\n"))

totallpasslength = numberofletters + Symbols + Numbers

# easy lvl

# password = ""

# for char in range(1 , numberofletters + 1):
#     randomchar = random.choice(letters) 
#     password += randomchar

# for symbol in range(1 , Symbols + 1):
#     randomsymbols = random.choice(chars)
#     password += randomsymbols

# for number in range(1 , Numbers + 1):
#     randomnumbers = random.choice(numbers)
#     password += randomnumbers

# print(password)

# hard level


password = []

for char in range(1 , numberofletters + 1):
    randomchar = random.choice(letters) 
    password.append(randomchar)

for symbol in range(1 , Symbols + 1):
    randomsymbols = random.choice(chars)
    password.append(randomsymbols)

for number in range(1 , Numbers + 1):
    randomnumbers = random.choice(numbers)
    password.append(randomnumbers)

# passby = random.shuffle(password)
# print(passby) dont now why it is not working !

realpass = ""

for passchat in range(1 , totallpasslength + 1):
    randompass = random.choice(password)
    realpass += randompass

print(f"your strongest pass is here {realpass}")

