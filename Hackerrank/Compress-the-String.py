# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

S = str(raw_input())
T = [list(g) for k, g in groupby(S)]

for i in T:
    print (len(i), int(i[0])),

