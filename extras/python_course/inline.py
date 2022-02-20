##spam = ['apples', 'bananas', 'tofu', 'cats']
##
##def putInLine(spam):
##    out = ''
##    size = len(spam)
##    for i in range(size):      # 4      0 1 2 3
##        if i < size-2:
##            character = ', '
##        elif i == size-2:
##            character = ' and '
##        else:
##            character = ''
##        out = out + spam[i] + character
##    return out
##
##print(putInLine(spam))

# 6 9

grid = [['.','.','.','.','.','.'],
        ['.','O','O','.','.','.'],
        ['O','O','O','O','.','.'],
        ['O','O','O','O','O','.'],
        ['.','O','O','O','O','O'],
        ['O','O','O','O','O','.'],
        ['O','O','O','O','.','.'],
        ['.','O','O','.','.','.'],
        ['.','.','.','.','.','.']]

# x = [[None]*3]*3
# x =[ [0 for x in range(3)] for y in range(3)]

# Original
for renglon in range(9):
    for columna in range(6):
        print(grid[renglon][columna],end='')
    print('')
    
##for columna in range(6):
##    for renglon in range(9):
##        print(grid[renglon][columna],end='')
##    print('')


# Rotar a la derecha
for columna in range(6):
    for renglon in range(8,-1,-1):
        print(grid[renglon][columna],end='')
    print('')

# Rotar a la izquierda
for columna in range(5,-1,-1):
    for renglon in range(9):
        print(grid[renglon][columna],end='')
    print('')

