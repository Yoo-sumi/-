import sys
input=sys.stdin.readline
n=int(input())
array=[]

for _ in range(n):
    a,b=map(int,input().split())
    array.append((a,b))
array.sort(key=lambda x:(x[1],x[0]))
for a,b in array:
    print(a,b)