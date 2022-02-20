spam = ['apples', 'bananas', 'tofu', 'cats']

def putInLine(spam):
    out = ''
    size = len(spam)
    for i in range(size):      # 4      0 1 2 3
        if i < size-2:
            character = ', '
        elif i == size-2:
            character = ' and '
        if i == size-1:
            character = ''
        out = out + spam[i] + character
    return out

print(putInLine(spam))
