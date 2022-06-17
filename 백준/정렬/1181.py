import sys
input=sys.stdin.readline
n=int(input())
array=[]
for _ in range(n):
    word="".join(input().split())
    array.append((len(word),word))
array.sort(key=lambda x:(x[0],x[1]))
print(array)
result=[]
for a,b in array:
    if not b in result:
        result.append(b)
        print(b)