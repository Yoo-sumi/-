from collections import deque
def solution(priorities, location):
    answer = 0
    result=[]
    q=deque()
    for i in range(len(priorities)):
        q.append((priorities[i],i))
    while q:
        now=q.popleft()
        flag=False
        for i in q:
            if now[0]<i[0]:
                flag=True
                break
        if flag==True:
            q.append(now)
            continue
        result.append(now[1])
    for i in range(len(result)):
        if result[i]==location:
            answer=i+1
    return answer
print(solution([2, 1, 3, 2],2))
'''
priorities	location	return
[2, 1, 3, 2]	2	1
[1, 1, 9, 1, 1, 1]	0	5
'''