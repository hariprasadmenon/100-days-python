alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def ceaser(plain_text, shift_amount, user_direction):
  final_msg = []
  shift_amount*= -1 if user_direction =="decode" else shift_amount
  for i in text:
      if i == " ":
          final_msg.append(" ")
      elif alphabet.index(i) + shift_amount < 0:
          letter = alphabet.index(i)
          final_msg.append(alphabet[letter+shift_amount+26])
      elif alphabet.index(i) + shift_amount > 25:
          letter = alphabet.index(i)
          final_msg.append(alphabet[letter+shift_amount-26])
      else:
          letter = alphabet.index(i)
          final_msg.append(alphabet[letter+shift_amount])
  if user_direction == "encode":
    print(f"The encoded text is {''.join(final_msg)}")
  else:
    print(f"The decoded text is {''.join(final_msg)}")
ceaser(plain_text = text, shift_amount = shift, user_direction = direction)
