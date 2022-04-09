import sys
input=sys.stdin.readline
n=int(input())
array={}
arr=[]
s=0
result=[]
for _ in range(n):
    i=int(input())
    s+=i
    arr.append(i)
    array[i]=array.get(i,0)+1

keys=sorted(array.keys())
arr.sort()
print(round(s/n))
print(arr[len(arr)//2])
for i in keys:
    if array[i]==max(array.values()):
        result.append(i)
result.sort()
if len(result)>1:
    print(result[1])
else:
    print(result[0])
print(keys[-1]-keys[0])