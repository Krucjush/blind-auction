import art
import os
print(art.logo)

auction = {}
run = True

def clean():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

while run:
    name = input('What is your name?: ')
    bid = input('What is your bid?: $')
    auction[name] = float(bid)
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other_bidders not in ['yes', 'no']:
        exit(f'{other_bidders} is not a valid command.\nAborting...')
    if other_bidders == 'no':
        run = False
    clean()

max_bid = 0
winning_bidder = ''
 
for name in auction:
    if auction[name] > max_bid:
        max_bid = auction[name]
        winning_bidder = name

print(f'The winner is {winning_bidder} with a bid of ${max_bid}')