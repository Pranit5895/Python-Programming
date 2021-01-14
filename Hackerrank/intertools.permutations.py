# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

S = raw_input().split()

for i in sorted(permutations(S[0], int(S[1]))):
    print ''.join(i)

