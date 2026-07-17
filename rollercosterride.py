height = int(input("what is your height in cm"))

if height > 80:
    print("you can ride")
    age = int(input("what is your age"))
    wantphoto = input("do you want phot during ride yes or no ?")
    if age > 12 and age < 18:
        print("pay 7$ for ride")
    elif age <= 12:
        print("pay 5$ for ride")
    elif age >= 45 and age <= 55:
        print("everthing is ok , have a free ride on us !")
    else:
        print("pay 10$ for ride")

    if wantphoto == "yes":
        print("extra 3$ will be charged for photo")
    else : 
        print("no extra money will be charged") 
else:
    print("not eligible")
