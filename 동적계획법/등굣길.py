def p(array):
    for i in array:
        for j in i:
            print(j, end=" ")
        print()
def solution(m, n, puddles):
    array=[[0]*(m+1) for _ in range(n+1)]
    array[1][1]=1
    for i in puddles:
        array[i[1]][i[0]]=-1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if array[i][j]==-1:
                continue
            if i==1 and j==1:
                continue
            if array[i][j-1]==-1 or array[i-1][j]==-1:
                array[i][j]=max(array[i-1][j],array[i][j-1])
            elif array[i][j-1]==-1 and array[i-1][j]==-1:
                array[i][j]=0
            else:
                array[i][j]=array[i][j-1]+array[i-1][j]
    return array[n][m]%1000000007
print(solution(4,3,[[2,2]]))
'''
m	n	puddles	return
4	3	[[2, 2]]	4
'''