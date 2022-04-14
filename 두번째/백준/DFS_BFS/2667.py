import sys
input=sys.stdin.readline

n=int(input())
graph=[[0]*(n) for _ in range(n)]

for i in range(n):
    li=list(input())
    for j in range(n):
        graph[i][j]=int(li[j])

def dfs(x,y,count):
    global graph
    if graph[x][y]!=1:
        return
    graph[x][y]=count
    if y!=0:
        dfs(x,y-1,count)
    if y!=n-1:
        dfs(x,y+1,count)
    if x!=0:
        dfs(x-1,y,count)
    if x!=n-1:
        dfs(x+1,y,count)

count=1
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            count+=1
            dfs(i,j,count)


result=[0]*(count-1)
for i in range(n):
    for j in range(n):
        if graph[i][j]>1:
            result[graph[i][j]-2]+=1
print(count-1)
result.sort()
for i in result:
    print(i)
