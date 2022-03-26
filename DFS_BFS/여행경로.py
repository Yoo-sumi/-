def solution(tickets):
    dic = {}
    #tickets 데이터로 dictionary 생성 - 키:출발도시,값:도착도시리스트
    for ticket in tickets:
        dic[ticket[0]] = dic.get(ticket[0], []) + [ticket[1]]
    for key in dic.keys(): #dic의 값 리스트 값을 역순정렬
        dic[key].sort(reverse=True)
    print(dic)
    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]
        print(stack)
        if top not in dic or len(dic[top]) == 0: #dic에 없거나, 있어도 더이상 도착지가 없으면
            path.append(stack.pop()) #path에 추가
        else:
            stack.append(dic[top][-1]) #stack에 추가
            dic[top].pop() #삭제
    return path[::-1]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
#print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
'''
tickets	return
[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	["ICN", "JFK", "HND", "IAD"]
[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
'''