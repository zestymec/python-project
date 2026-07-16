height = 1.65
weight = 84
bmi = weight/(height**2) 
print(f"you bmi is {bmi}")
if bmi > 18.5:
    print("normal")
elif bmi < 25:
    print("normal")
else:
    print("you are overweight")