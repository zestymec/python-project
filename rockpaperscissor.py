import random

rock = r"""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
"""
paper = r"""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
"""
scissor = r"""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
"""

userchoice = int(
    input("What do you choose? Type 0 for Rock , 1 for Paper or 2 for  Scissors.")
)

computerchoice = random.randrange(0, 3)

if computerchoice == 0:
    print(f"computer choice is {rock}")
elif computerchoice == 1:
    print(f"computer choice is {paper}")
elif computerchoice == 2:
    print(f"computer choice is {scissor}")
if userchoice == 0:
    print(f"user choice is {rock}")
elif userchoice == 1:
    print(f"user choice is {paper}")
elif userchoice == 2:
    print(f"user choice is {scissor}")
if userchoice >= 3 or userchoice < 0:
    print("invalid statement")
elif userchoice == 0 and computerchoice == 2:
    print("You wine")
elif computerchoice > userchoice:
    print("computer wins!")
elif userchoice > computerchoice:
    print("You win")
elif computerchoice == userchoice:
    print("Draw")
elif computerchoice == 0 and userchoice == 2:
    print("you lose ")
else:
    print("invalid statement")
