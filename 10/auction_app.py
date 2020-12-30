from clear_screen import clear
from auction_art import logo


def find_highest_bidder(bidding_record):

    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]

        if bid_amount > highest_bid:

            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of R{highest_bid}")


bids = {}
bidding_finished = False

print(logo)
print('Welcome To The Auction!')

while not bidding_finished:

    name = input("What is your name?: ")
    price = int(input("What is your bid?: R"))
    bids[name] = price
    should_continue = input(
        "Are there any other bidders? Yes or No \n").lower()

    if should_continue == "no":

        bidding_finished = True
        find_highest_bidder(bids)

    elif should_continue == "yes":
        clear()
