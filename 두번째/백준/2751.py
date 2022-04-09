import sys
input=sys.stdin.readline
n=int(input())
array={}
for _ in range(n):
    i=int(input())
    array[i]=array.get(i,0)+1
keys=sorted(array.keys())
print(keys)
for i in keys:
    for j in range(array[i]):
        print(i)
