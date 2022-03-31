from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    q=deque()
    for i in range(len(speeds)):
        q.append(math.ceil((100-progresses[i])/speeds[i]))

    count=0
    before=math.ceil((100-progresses[0])/speeds[0])
    while q:
        now=q.popleft()
        if now<=before:
            count+=1
            continue
        answer.append(count)
        count=1
        before=now
    answer.append(count)
    return answer

print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
'''
progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
'''