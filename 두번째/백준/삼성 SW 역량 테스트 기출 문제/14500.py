import sys
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[] for _ in range(n)]
for i in range(n):
    graph[i]=(list(map(int,input().split())))
result=0
for x in range(n):
    for y in range(m):
        li=[[(x,y),(x,y+1),(x+1,y),(x+1,y+1)],
            [(x,y),(x,y+1),(x,y+2),(x,y+3)],[(x,y),(x+1,y),(x+2,y),(x+3,y)],
            [(x,y),(x,y+1),(x,y+2),(x+1,y+1)],[(x,y+1),(x+1,y),(x+1,y+1),(x+2,y+1)],[(x,y+1),(x+1,y),(x+1,y+1),(x+1,y+2)],[(x,y),(x+1,y),(x+1,y+1),(x+2,y)],
            [(x,y),(x+1,y),(x+1,y+1),(x+2,y+1)],[(x,y+1),(x,y+2),(x+1,y),(x+1,y+1)],
            [(x,y),(x+1,y),(x+2,y),(x+2,y+1)],[(x,y),(x,y+1),(x,y+2),(x+1,y)],[(x,y),(x,y+1),(x+1,y+1),(x+2,y+1)],[(x,y+2),(x+1,y),(x+1,y+1),(x+1,y+2)],
            [(x,y+1),(x+1,y),(x+1,y+1),(x+2,y)],[(x,y),(x,y+1),(x+1,y+1),(x+1,y+2)],
            [(x,y+1),(x+1,y+1),(x+2,y+1),(x+2,y)],[(x,y),(x+1,y),(x+1,y+1),(x+1,y+2)],[(x,y),(x+1,y),(x+2,y),(x,y+1)],[(x,y),(x,y+1),(x,y+2),(x+1,y+2)]]
        for l in li:
            value=0
            for a,b in l:
                if not 0<=a<n or not 0<=b<m:
                    value=0
                    break
                value+=graph[a][b]
            result=max(result,value)
print(result)