from itertools import combinations
import copy
n,m=map(int,input().split())
graph=[[]*n for _ in range(n)]
chicken=[]
for i in range(n):
    li=list(map(int,input().split()))
    graph[i]=li
    for j in range(n):
        if li[j]==2:
            chicken.append((i,j))
li=list(combinations(chicken,m))

answer=1e9
for c in list(li):
    temp=[[1e9]*n for _ in range(n)]
    for cx,cy in c:
        for i in range(n):
            for j in range(n):
                if graph[i][j]==1:
                    temp[i][j]=min(temp[i][j],abs(cx-i)+abs(cy-j))
    result=0
    for i in range(n):
        for j in range(n):
            if temp[i][j]!=1e9:
                result+=temp[i][j]
    answer=min(answer,result)
print(answer)



