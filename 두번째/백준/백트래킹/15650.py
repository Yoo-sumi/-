import sys
from itertools import permutations
input=sys.stdin.readline

n,m=map(int,input().split())
array=[i for i in range(1,n+1)]
result=list(permutations(array,m))
for i in result:
    for j in i:
        print(j, end=" ")
    print()