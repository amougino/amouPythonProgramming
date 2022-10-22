import random

def GiveARandomCard():

    i = random.randint(0,51)

    cards0 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']
    cards = [ card+t for t in ['_spades', '_hearts', '_diamonds', '_clubs'] for card in cards0 ]

    return cards[i]

test = GiveARandomCard()

print(test)