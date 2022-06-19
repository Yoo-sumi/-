def solution():
    n,k=map(int,input().split())
    s=""
    for i in range(1,n+1):
        s+=str(i)
    s=list(s)
    if len(s)<k:
        return -1
    return int(s[k-1])
print(solution())

