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