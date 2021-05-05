from replit import clear
from art import logo

#Calculator

def add(n1,n2):
  return n1 + n2
def subtract(n1,n2):
  return n1 - n2
def multiply(n1,n2):
  return n1 * n2
def divide(n1,n2):
  return n1 / n2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol) 
  operation_symbol = input("Pick an operation from the line above: ")
  num2 = float(input("What's the second number?: "))
  calc_function = operations[operation_symbol]
  answer = calc_function(num1,num2)

  print(f"{num1} {operation_symbol} {num2} = {answer}")

  continue_calc = True
  while continue_calc == True:
    user_choice = input("Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
    if user_choice == "y":
      operation_symbol = input("Pick an operation: ")
      num1_new = answer
      num2_new = float(input("What's the next number?: "))
      calc_function = operations[operation_symbol]
      answer = calc_function(num1_new,num2_new)
      print(f"{num1_new} {operation_symbol} {num2_new} = {answer}")
    elif user_choice == "n":
      continue_calc = False
      clear()
      calculator()
calculator()
