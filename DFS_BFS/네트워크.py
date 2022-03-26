from collections import deque
def solution(n, computers):
    answer = 0
    q=deque()
    flag=[False]*len(computers)
    for i in range(n):
        if not False in flag:
            break
        if flag[i]==True:
            continue
        q.append(i)
        flag[i]=True
        while q:
            now=q.popleft()
            for j in range(n):
                if computers[now][j]==1 and flag[j]==False:
                    q.append(j)
                    flag[j]=True
        answer+=1
    if False in flag:
        answer+=flag.count(False)
    return answer

print(solution(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]))
'''
n	computers	return
3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1
'''