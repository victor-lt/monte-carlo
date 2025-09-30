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

def play-round(profile, bet)
    player-hand = [draw(card), draw(card)] #draw first 2 cards
    dealer-hand = [draw(card), draw(card)]
    '''
        -----add insurance management-----
    '''
    if check-split(player_hand): #return true if the player split, false if not
        return split(player-hand, dealer-hand)
    player-hand = player-gameplay(player-gameplay) #return the hand of the player at the end of his turn
    return bet*is-winner(player-hand, dealer-hand) #is-winner return 1 or -1 (HAVE TO ADD INSURANCE MONEY)
