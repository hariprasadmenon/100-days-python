import replit
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
other = [' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def caeser(plain_text, shift_amount, user_direction):
    if shift_amount >= 26:
      shift_amount = shift_amount%26
    final_msg = []
    if user_direction =="decode":
      shift_amount*= -1
    for i in text:
        if i in other:
            final_msg.append(i)
        elif alphabet.index(i) + shift_amount < 0:
            letter = alphabet.index(i)
            final_msg.append(alphabet[letter+shift_amount+26])
        elif alphabet.index(i) + shift_amount > 25:
            letter = alphabet.index(i)
            final_msg.append(alphabet[letter+shift_amount-26])
        else:
            letter = alphabet.index(i)
            final_msg.append(alphabet[letter+shift_amount])

    print(f"The {user_direction}d text is: {''.join(final_msg)}")

go_again = "yes"
while go_again == "yes":
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(plain_text=text, shift_amount=shift, user_direction=direction)
    go_again = input("Do you want to continue, 'yes' or 'no'?: ").lower()
    if go_again == "yes":
      replit.clear()
    else:
      print("Goodbye!")

