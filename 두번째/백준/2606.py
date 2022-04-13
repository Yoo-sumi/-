import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
graph=[[] for _ in range(n+1)]
flag=[False]*(n+1)
v=int(input())
q=deque()

for _ in range(v):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(node):
    q.append(node)
    flag[node]=True
    while q:
        now=q.popleft()
        for i in graph[now]:
            if flag[i]==False:
                q.append(i)
                flag[i]=True
    print(flag.count(True)-1)

bfs(1)

