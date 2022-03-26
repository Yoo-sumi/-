from collections import deque
def solution(begin, target, words):
    if not target in words:
        return 0
    q=deque()
    flag=[[] for _ in range(len(words))]
    q.append((begin,0))
    value=len(words)+1
    while q:
        now=q.popleft()
        if now[0]==target:
            value=min(value,now[1])
            continue
        for i in range(len(words)):
            c=0
            for j in range(len(begin)):
                if now[0][j]!=words[i][j]:
                    c+=1
            if c==1:

                if now[0]!=begin and words[i] in flag[words.index(now[0])]:
                    continue
                q.append((words[i],now[1]+1))
                flag[i].append(now[0])
    if value>len(words):
        return 0
    return value
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]	))
'''
begin	target	words	return
"hit"	"cog"	["hih", "dot", "dog", "lot", "log", "cog"]	4
"hit"	"cog"	["hot", "dot", "dog", "lot", "log"]	0
'''