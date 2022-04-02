def solution(n, computers):
    answer = 0
    flag=[]
    stack=[]
    for i in range(n):
        if not i in flag:
            stack.append(i)
            flag.append(i)
            answer+=1
        else:
            continue
        while stack:
            now=stack.pop()
            for j in range(n):
                if computers[now][j]==1 and not j in flag:
                    stack.append(j)
                    flag.append(j)
    return answer
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
'''
n	computers	return
3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1
'''