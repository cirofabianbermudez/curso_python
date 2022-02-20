##import pprint
##
##theBoard  = {'low-L': ' ',
##             'low-M': ' ',
##             'low-R': ' ',
##             'mid-L': ' ',
##             'mid-M': ' ',
##             'mid-R': ' ',
##             'top-L': ' ',
##             'top-M': ' ',
##             'top-R': ' '
##             }
##
##pprint.pprint(theBoard)
##
##def printBoard(board):
##    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] + '|' )
##    print('--------' )
##    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'] + '|' )
##    print('--------' )
##    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'] + '|' )
##    print('\n')
##    return None
##
##printBoard(theBoard)
##
##theBoard['top-L'] = 'X'
##
##printBoard(theBoard)
##    


allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
            'Bob': {'ham sandwiches': 3, 'apples': 2},
            'Carol': {'cups': 3, 'apple pies': 1}}


def totalBrought(guests):
    allItems = {}
    numBrought = 0
    for k, v in guests.items():
        for k1, v1 in v.items():
            allItems.setdefault(k1, 0)
            allItems[k1] += v1 
    print(allItems)
    return None

totalBrought(allGuests)


