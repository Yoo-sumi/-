import sys
from collections import deque
input=sys.stdin.readline
n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()

flag=[False]*(n+1)

def dfs(node,flag):
    print(node,end=" ")
    for i in graph[node]:
        if flag[i]==False:
            flag[i]=True
            dfs(i,flag)

flag[v]=True
dfs(v,flag)
print()
def bfs(node):
    while q:
        now=q.popleft()
        print(now,end=" ")
        for i in graph[now]:
            if flag[i]==False:
                q.append(i)
                flag[i]=True


flag=[False]*(n+1)
q=deque()
q.append(v)
flag[v]=True
bfs(v)



