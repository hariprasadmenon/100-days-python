import operator
from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
active_bid = {}
auction_open = True
def add_bid(current_name, current_bid):
  active_bid[current_name] = current_bid

while auction_open == True:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  add_bid(current_name=name, current_bid=bid)
  more_bid = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  if more_bid == "yes":
    clear()
  else:
    auction_open = False
    clear()
#high_bid = max(active_bid.items(), key=operator.itemgetter(1))[0]
bid_amount = 0
for x in active_bid:
  if active_bid[x] > bid_amount:
    bid_amount = active_bid[x]
    high_bid = x
print(f"The winner is {high_bid} with a bid of ${active_bid[high_bid]}")
