n=int(input())
array=[]
for _ in range(n):
    a,b=map(int,input().split())
    array.append((a,b))
result=[]
for i in range(n):
    count=0
    for j in range(n):
        if i==j:
            continue
        if array[i][0]<array[j][0] and array[i][1]<array[j][1]:
            count+=1
    result.append(count+1)
for i in result:
    print(i,end=" ")