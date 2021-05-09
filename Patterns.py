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

def pattern4(level):
    '''This function prints the following pattern:
    ****
     ***
      **
       *
    '''
    counter = 0
    for i in range(level, 0 ,-1):
        print(' ' * counter + '*' * i)
        counter += 1

def pattern5(level):
    '''This function prints the following pattern:
      *
     ***
    *****
    '''
    # first loop for number of lines
    for i in range(level + 1):
        #second loop for spaces
        for j in range(level - i):
            print (" ",end='')
        # this loop is for printing stars
        for k in range(2 * i - 1):
            print("*", end='')
        print()

if __name__ == '__main__':
    userInput = int(input('Enter the level: '))