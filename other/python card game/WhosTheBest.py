

def WhosTheBest(card1,card2):
    value1 = card1.split('_')[0]
    if value1 == 'JACK':
        value1 = 11
    elif value1 == 'QUEEN':
        value1 = 12
    elif value1 == 'KING':
        value1 = 13
    else :
        value1 = int(value1)

    value2 = card2.split('_')[0]
    if value2 == 'JACK':
        value2 = 11
    elif value2 == 'QUEEN':
        value2 = 12
    elif value2 == 'KING':
        value2 = 13
    else :
        value2 = int(value2)

    if value1 > value2:
        print ('Player 1 Wins!',card1,'>',card2)
    elif value1 == value2:
        print ('Tie!',card1,'=',card2)
    else :
        print ('Player 2 Wins!',card1,'<',card2)
