import sys
sys.setrecursionlimit(10 ** 4)
input=sys.stdin.readline

t=int(input())

def dfs(x,y):
    if graph[x][y]!=1:
        return
    graph[x][y]=-1
    if y!=0:
        dfs(x,y-1)
    if y!=m-1:
        dfs(x,y+1)
    if x!=0:
        dfs(x-1,y)
    if x!=n-1:
        dfs(x+1,y)
result=[]
for _ in range(t):
    m,n,k=map(int,input().split())
    graph=[[0]*(m) for _ in range(n)]
    for _ in range(k):
        x,y=map(int,input().split())
        graph[y][x]=1
    count=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                dfs(i,j)
                count+=1
    result.append(count)

for i in result:
    print(i)