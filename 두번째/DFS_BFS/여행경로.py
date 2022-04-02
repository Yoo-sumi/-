def solution(tickets):
    answer = []
    dic={}
    for a,b in tickets:
        dic[a]=sorted(dic.get(a,[])+[b],reverse=True)
    q=[]
    q.append("ICN")
    while q:
        now=q[-1]
        if dic.get(now,-1)==-1 or not dic.get(now):
            answer.append(q.pop())
        else:
            q.append(dic.get(now).pop())
    return answer[::-1]
print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"]]))
'''
tickets	return
[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	["ICN", "JFK", "HND", "IAD"]
[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
'''