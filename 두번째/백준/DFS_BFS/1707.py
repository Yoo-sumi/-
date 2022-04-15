import sys
from collections import deque

def bfs(graph,visited):
    q = deque()
    group = 1
    bipatite = True
    for i in range(1, len(visited)):
        if visited[i] == 0: # 방문하지 않은 정점이면 bfs 수행
            q.append(i)
            visited[i] = group
            while q:
                v = q.popleft()
                for w in graph[v]:
                    if visited[w] == 0: # 방문하지 않은 정점이면 큐에 삽입
                        q.append(w)
                        visited[w] = -1 * visited[v] # 현재 노드와 다른 그룹 지정
                    elif visited[v] == visited[w]: # 이미 방문한 경우, 동일한 그룹에 속하면 False
                        bipatite = False
    """q=deque()
    flag=True
    for h in range(1,v+1):
        if visited[h]==0:
            q.append(1)
            visited[1]=1
            while q:
                now=q.popleft()
                for i in graph[now]:
                    if visited[i]==0:
                        if visited[now]==1:
                            visited[i]=-1
                        elif visited[now]==-1:
                            visited[i]=1
                        q.append(i)
                    elif visited[now]==visited[i]:
                        flag=False

    return "YES" if flag else "NO"""

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
    result.append(bfs(graph,visited))
for i in result:
    print(i)