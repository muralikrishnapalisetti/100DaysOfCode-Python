# secret_auction.py

print(r"""                         ___________
                         \         /
                          )_______(
                          |'''''''|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )'''''''(
                         /_________\ 
                         `'-------'`
                       .-------------.
                      /_______________\ """)


def clear_screen():
    print("\n" * 100)
# Function to find the highest bidder


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"\nThe winner is {winner} with a bid of ₹{highest_bid}!")


# Main program
print("Welcome to the Secret Auction Program!")

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    bid_price = int(input("What is your bid price (₹)?: "))
    bids[name] = bid_price

    more_bidders = input("Are there any other users who want to bid? Type 'yes' or 'no': ").lower()
    if more_bidders == "yes":
        clear_screen()  # Clear screen for the next bidder
    else:
        bidding_finished = True
        find_highest_bidder(bids)
