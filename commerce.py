Age = int(input("what is your age?"))
Gender = input("what is your gender if boy do write b if girl so write g !")
hairs = input("your hairs short or long")
if Age >= 18:
    print("you are allowed to go in web")
    if Gender == "b":
        print("mens wear")
    elif Gender == "g":
        print("womerns wear")
        if hairs == "short":
            print("short hijab")
        else:
            print("hijab")
    else:
        print("javkets")
elif Age > 16:
    print("jackets")
    if Gender == "b":
        print("mens wear")
    elif Gender == "g":
        print("womerns wear")
    else:
        print("javkets")
elif Age > 40:
    print("shirts")
else:
    print("You are not Allowed!")
