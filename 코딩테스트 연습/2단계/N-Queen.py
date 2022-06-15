def dfs(queen,row,n):
    count=0
    if row==n:
        return 1
    for i in range(n):
        queen[row]=i
        flag=True
        for j in range(row):
            if queen[row]==queen[j]:
                flag=False
                break
            if abs(queen[row]-queen[j])==abs(row-j):
                flag=False
                break
        if flag:
            count+=dfs(queen,row+1,n)
    return count
def solution(n):
    return dfs([0]*n,0,n)