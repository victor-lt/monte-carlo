Jbase = [

[[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None], [ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None]], #4
[[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None], [ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None]], #5
[[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None], [ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None]], #6
[[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None], [ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None]], #7
[[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None], [ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None]], #8
[[ 'T', None, None, None],[ 'D', None, None, None],[ 'D', None, None, None],[ 'D', None, None, None],[ 'T', None, None, None], [ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None]], #9
[[ 'D', None, None, None],[ 'D', None, None, None],[ 'D', None, None, None],[ 'D', None, None, None],[ 'D', None, None, None], [ 'D', None, None, None],[ 'D', None, None, None],[ 'D', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None]], #10
[[ 'D', None, None, None],[ 'D', None, None, None],[ 'D', None, None, None],[ 'D', None, None, None],[ 'D', None, None, None], [ 'D', None, None, None],[ 'D', None, None, None],[ 'D', None, None, None],[ 'D', None, None, None],[ 'T', None, None, None]], #11
[[ 'T', None, None, None],[ 'T', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None], [ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None]], #12
[[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None], [ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None]], #13
[[ 'T', None, None, None],[ 'T', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None], [ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None]], #14
[[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None], [ 'T', None, None, None],[ 'R', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None]], #15
[[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None], [ 'T', None, None, None],[ 'R', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None],[ 'T', None, None, None]], #16
[[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None], [ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None]], #17
[[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None], [ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None]], #18
[[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None], [ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None]], #19
[[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None], [ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None],[ 'R', None, None, None]], #20

]

prandom = {"name": "random", 'counted': 0} #player who plays randomly
#rules = [split after aces, split after split, hit on soft 17, deck number, penetration (0-1 ratio) ] all bools except last one
basic_rules = [False, True, True, 8, .6]

def draw_card(shoe, hand):
    card = shoe.pop()
    if card == 11:
        hand[1] += 1
    if hand[0] + card > 21:
        if hand[1] >= 1:
            hand[0] -= 10
            hand[1] = 1
    return card

def has_player_won(player, dealer):
    if player > 21:
        return 0
    elif dealer > 21:
        return 2
    elif player > dealer:
        return 2
    elif player == dealer:
        return 1
    else:
        return 0

def play_hand(player, rules, shoe):
    
    phand = [0, 0, False] #hand = (value, ace number, is it a pair)
    dhand = [0, 0]

    card1 = draw_card(phand, shoe)
    card2 = draw_card(phand, shoe)

    if card1 == card2:
        phand[2] = True

    draw_card(dhand[0], shoe[0])
    draw_card(dhand, shoe)

    player_time(player, phand, dhand, rules)

    return has_player_won(phand[0], dhand[0])

def init_shoe(shoe_nb):
    shoe = []
    for i in range(shoe_nb*52):
        j = i%13
        if j == 0:
            shoe.append(11)
        elif j < 9:
            shoe.append(j)
        elif j >= 9:
            shoe.append(10)

    #apply shuffle function to shoe
    return shoe

def choose_bet(player):
    if player['name'] == 'random':
        return 1

def play_shoe(player, rules):
    shoe = init_shoe(rules[3])
    bankroll = 0
    while len(shoe) >= (1-rules[4])*52:
        bet = choose_bet(player)
        bankroll += bet*play_hand(player, rules, shoe)
    return bankroll

def player_time(player, phand, dhand, rules):
    pass

def interface(player, shoe_nb, rules):
    bankroll = 0
    for i in range(shoe_nb):
        bankroll += play_shoe(player, rules)
    return bankroll


print(interface(prandom, 8, basic_rules))