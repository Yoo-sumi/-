import sys
input=sys.stdin.readline
n=int(input())
array=[]

for i in range(n):
    a,b=map(str,input().split())
    array.append((int(a),i,b))
array.sort(key=lambda x:(x[0],x[1]))
for i in array:
    print(i[0],i[2])
