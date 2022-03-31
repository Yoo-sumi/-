'''def solution(prices):
    answer = []
    q=[]+prices
    q.reverse()
    while q:
        now=q.pop()
        count=0
        for i in range(len(q)-1,-1,-1):
            count+=1
            if now>q[i]:
                break
        answer.append(count)
    return answer'''
from collections import deque
def solution(prices):
    answer = []
    q=deque(prices)
    while q:
        now=q.popleft()
        count=0
        for i in q:
            count+=1
            if now>i:
                break
        answer.append(count)
    return answer
print(solution([1, 2, 3, 2, 3]))
'''
prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
'''