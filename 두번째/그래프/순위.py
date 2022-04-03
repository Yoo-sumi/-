def solution(n, results):
    answer = 0
    array=[[0]*n for _ in range(n)]
    for a,b in results:
        array[a-1][b-1]=1
        array[b-1][a-1]=-1
    print(array)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if array[i][j] in [1,-1] or i==j:
                    continue
                if array[i][k]==array[k][j]==1:
                    array[i][j]=1
                    array[j][i]=-1
    for i in array:
        if i.count(0)==1:
            answer+=1
    return answer
print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
'''
n	results	return
5	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	2
'''