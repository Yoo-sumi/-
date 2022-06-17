import math
n=int(input())
array=list(map(int,input().split()))
b,c=map(int,input().split())

for i in range(n):
    array[i]-=b
result=[]
for i in range(n):
    if array[i]<=0:
        result.append(1)
    else:
        result.append(math.ceil(array[i]/c)+1)
print(sum(result))