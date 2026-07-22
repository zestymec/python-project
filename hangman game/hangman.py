import random
import words
from levels import stagesofd


print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/       """)


randomword = ""
randomword = random.choice(words.hangman_words)
randomwordlen = len(randomword)

lines = ""
while len(randomword) != len(lines):
    lines += "_"

lives = 6
correctletters = []
game = ""

while game == "":
    guess = input(f"guess the letter : {lines}\n").lower()
    
    display = ""
    for letter in randomword:
        if letter == guess:
            display += letter
            correctletters.append(guess)
        elif letter in correctletters:
            display += letter
        else:
            display += "_"
    print(display)
    if guess in correctletters:
        print(f"you already guess {guess}")
    if guess not in randomword:
        lives -= 1
        print(f"{guess} is not in this words thats why you lose a life")
    print(f"{lives}/6 LIVES LEFT")
    print(stagesofd[lives])
    if "_" not in display:
        print("You win.")
        game = "over"
    elif lives == 0:
        game = "over"
        print(f"all chance are gone! and the word is {randomword}")
