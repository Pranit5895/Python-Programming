# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, raw_input().split(' '))

# top 
for i in range(1, (n / 2) + 1):  
    print ('.|.' * ((i * 2) - 1)).center(m, '-')  
    
# welcome  
print 'WELCOME'.center(m, '-')  

# bottom  
for i in range(((n - 1) / 2), 0, -1):  
    print ('.|.' * ((i * 2) - 1)).center(m, '-')  

