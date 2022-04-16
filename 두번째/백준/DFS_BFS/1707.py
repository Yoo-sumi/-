import sys
from collections import deque
input=sys.stdin.readline

def bfs(graph,visited):
    q=deque()
    flag=True
    for h in range(1,len(visited)):
        if visited[h]==0:
            q.append(h)
            visited[h]=1
            while q:
                now=q.popleft()
                for i in graph[now]:
                    if visited[i]==0:
                        visited[i]=-1*visited[now]
                        q.append(i)
                    elif visited[now]==visited[i]:
                        flag=False

    return "YES" if flag else "NO"

t=int(input())
result=[]
for _ in range(t):
    v,e=map(int,input().split())
    visited=[0]*(v+1)
    graph=[[] for _ in range(v+1)]
    for _ in range(e):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(bfs(graph,visited))