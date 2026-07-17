print("""
                                               /\      /\
                                               ||______||
                                               || ^  ^ ||
                                               \| |  | |/
                                                |______|
              __                                |  __  |
             /  \       ________________________|_/  \_|__
            / ^^ \     /=========================/ ^^ \===|
           /  []  \   /=========================/  []  \==|
          /________\ /=========================/________\=|
       *  |        |/==========================|        |=|
      *** | ^^  ^^ |---------------------------| ^^  ^^ |--
     *****| []  [] |           _____           | []  [] | |
    *******        |          /_____\          |      * | |
   *********^^  ^^ |  ^^  ^^  |  |  |  ^^  ^^  |     ***| |
  ***********]  [] |  []  []  |  |  |  []  []  | ===***** |
 *************     |         @|__|__|@         |/ |*******|
***************   ***********--=====--**********| *********
***************___*********** |=====| **********|***********
 *************     ********* /=======\ ******** | *********
""")

print("Welcome to Treasure Island")
print("your mission is to find the treasure")
leftorright = input("left or right ?").lower()
if leftorright == "left":
    swimorwait = input("swim or wait for boat")
    if swimorwait == "wait":
        whichdoor = input("which door(red, blue or yellow)")
        if whichdoor == "red":
            print("burned by fire")
            print("Game Over")
        elif whichdoor == "blue":
            print("eaten by beats.")
            print("Game Over")
        elif whichdoor == "yellow":
            print("congratulations now you became a millionaire")
            print("you won the game !")
        else:
            print("Game Over")
    else:
        print("Attacked by trout")
        print("Game Over")
else:
    print("Fall into a hole .")
    print("Game Over")