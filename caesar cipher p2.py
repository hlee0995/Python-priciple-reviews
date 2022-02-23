from art import logo 

print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def caesar (plain_text, amount_shift):
    if direction == "encode": 
        new_text=""
        for letter in plain_text:
            if letter in alphabet:
                ind = alphabet.index(letter)
                new_ind = ind + shift
                if new_ind > 25:
                    new_ind -= 26
                new_letter = alphabet[new_ind]
                new_text += new_letter
            else:
                new_text += letter
        print(f"encoded message is {new_text}")
    elif direction == "decode":
        new_text=""
        for letter in plain_text:
            if letter in alphabet:
                ind = alphabet.index(letter)
                new_ind = ind - shift
                if new_ind < 0: 
                    new_ind += 26
                new_letter = alphabet[new_ind]
                new_text += new_letter
            else:
                new_text += letter
        print(f"decoded message is {new_text}")
    else: print("Wrong input")
          
        
token = True

while token == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift)
    result = input('Do you want to play again? Type "Yes" or "no"')
    if result == "no":
        token = False
