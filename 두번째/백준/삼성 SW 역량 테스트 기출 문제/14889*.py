from itertools import combinations
import copy
n=int(input())
graph=[[] for _ in range(n)]
array=[i for i in range(n)]
for i in range(n):
    graph[i]=list(map(int,input().split()))

li1=list(combinations(array,n//2))

result=1e9
for i in range(len(li1)//2):
    li2=list(combinations(list(li1[i]),2))
    s_total=0
    for a,b in li2:
        s_total+=graph[a][b]
        s_total+=graph[b][a]
    temp=copy.deepcopy(array)
    for h in li1[i]:
        temp.remove(h)
    li2=list(combinations(temp,2))
    l_total=0
    for a,b in li2:
        l_total+=graph[a][b]
        l_total+=graph[b][a]
    result=min(result,abs(s_total-l_total))
print(result)

