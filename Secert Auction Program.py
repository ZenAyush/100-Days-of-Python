from art import logo

print(logo)

bids = {}
bidding_finished = False

def highest_bidder (bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("Enter your name: ")
    bid_price = int(input("Enter you bid price: $"))

    bids[name] = bid_price
    # print(bids)

    should_contiune = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if should_contiune == "no":
        bidding_finished = True
        highest_bidder(bids)
    elif should_contiune == "yes":
        pass #clear the screen & continue the while loop