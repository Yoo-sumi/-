def solution(m, n, puddles):
    array=[[0]*(m+1) for _ in range(n+1)]
    array[1][1]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==j==1 or [j,i] in puddles:
                continue
            array[i][j]=array[i][j-1]+array[i-1][j]
    return array[n][m]
print(solution(4,3,[[2,2]]))
'''
m	n	puddles	return
4	3	[[2, 2]]	4
'''