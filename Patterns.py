def pattern1(level):
    '''This function prints the following pattern:
    *
    **
    ***
    ****
    '''
    for i in range(1, level + 1):
        print()
        for j in range(i):
            print('*', end = '')

def pattern2(level):
    '''This function prints the following pattern:
    ****
    ***
    **
    *
    '''
    for i in range(level, 0, -1):
        print()
        for j in range(i):
            print('*', end = '')

def pattern3(level):
    '''This function prints the following pattern:
       *
      **
     ***
    ****
    '''
    counter = level
    for i in range(level + 1):
        print(' ' * counter + '*' * i)
        counter -= 1