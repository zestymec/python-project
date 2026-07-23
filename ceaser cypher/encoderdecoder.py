from art import logo

def cipher():    
    print(logo)
    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
        'u', 'v', 'w', 'x', 'y', 'z'
    ]
    direction = input("Type 'encode' to encrypt and Type 'decode' for decrypt\n").lower()
    text = input("Type your message here:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def encrypt(originaltext , shift_amount):
        cipher_text = ""
        for letter in originaltext:
            if letter in alphabet:
                shiftedposition = alphabet.index(letter) + shift_amount
                shiftedposition = shiftedposition % len(alphabet)
                cipher_text += alphabet[shiftedposition]
            else:
                cipher_text += letter
        print(cipher_text)

    def decrypt(originaltext , shift_amount):
        cipher_text = ""
        for letter in originaltext:
            if letter in alphabet:
                shiftedposition = alphabet.index(letter) - shift_amount
                cipher_text += alphabet[shiftedposition]
            else:
                cipher_text += letter
        print(cipher_text)


    if direction == "encode":
        encrypt(originaltext=text , shift_amount=shift)
    elif direction == "decode":
        decrypt(originaltext=text , shift_amount=shift)
    else:
        print("invalid command")

    descision = input("do you want to encrypt more or decrypt more?").lower()
    if descision == "yes":
        cipher()
    else:
        print("thnx for coming here !")
cipher()
