from collections import deque
def solution(operations):
    q=deque()
    for i in operations:
        if i[0]=="I":
            q.append(int(i[2:]))
            q=deque(sorted(q))
        elif i[0]=="D":
            if not q:
                continue
            if int(i[2:])<0:
                q.popleft()
            else:
                q.pop()
    if not q:
        return [0,0]
    return [q[-1],q[0]]
print(solution(["I 7","I 5","I -5","D -1"]))
'''
operations	return
["I 16","D 1"]	[0,0]
["I 7","I 5","I -5","D -1"]	[7,5]
'''