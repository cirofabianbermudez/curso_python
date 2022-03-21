while True:
    print('How many cats do you have?')
    try:
        numCats = int(input())
        if numCats < 0:
            print('It doesnt make any sense, try again.')
        elif int(numCats) >= 4:
            print('That is a lot of cats.')
            break
        else:
            print('That is not many cats.')
            break
    except ValueError:
        print('Error: You did not enter a number.')
