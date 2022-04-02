def solution(begin, target, words):
    answer = 0
    if not target in words:
        return 0
    flag=[]
    q=[]
    q.append((begin,0))
    flag.append(begin)
    while q:
        now=q.pop()
        if now[0]==target:
            answer=now[1]
            break
        for i in words:
            count=0
            for j in range(len(begin)):
                if i[j]!=now[0][j]:
                    count+=1
            if count==1 and not i in flag:
                q.append((i,now[1]+1))
                flag.append(i)
    return answer
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log","cog"]))
'''
begin	target	words	return
"hit"	"cog"	["hot", "dot", "dog", "lot", "log", "cog"]	4
"hit"	"cog"	["hot", "dot", "dog", "lot", "log"]	0
'''