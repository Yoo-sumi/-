import sys
input=sys.stdin.readline

n,m=map(int,input().split())

s=[]

def dfs(s):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    for i in range(1,n+1):
        s.append(i)
        dfs(s)
        s.pop()
dic={}
a="abcdadf"
print(a[:-1])
dfs(s)