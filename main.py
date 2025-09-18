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

def piocher(main, sabot):
    carte = sabot.pop[0]
    (n, soft) = main
    if n + carte > 21:
        if soft <= 0: #Si la main n'a pas d'as
            return (0,0) #Convention: si la main[0] = 0 alors la main est bust
        else:
            return (main[0] + carte - 10, soft - 1)

def gagnant(main_joueur, main_croupier): #à terminer
    return None
