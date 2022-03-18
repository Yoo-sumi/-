from collections import deque
def solution(priorities, location):
    answer = 0
    value=[]
    q=deque()
    for i in range(len(priorities)):
        q.append((priorities[i],i))
        value.append(priorities[i])
    value.sort(reverse=True)
    index=1
    while q:
        now=q.popleft()
        max_value=value[0]
        if now[0]<max_value:
            q.append(now)
        else:
            if now[1]==location:
                answer=index
                break
            index+=1
            value.remove(value[0])
    return answer

solution([1, 1, 9, 1, 1, 1],0)
'''
priorities	location	return
[2, 1, 3, 2]	2	1
[1, 1, 9, 1, 1, 1]	0	5
'''