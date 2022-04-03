def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    result=set([costs[0][0]])
    while len(result)<n:
        for cost in costs:
            if cost[0] in result and cost[1] in result:
                continue
            if cost[0] in result or cost[1] in result:
                result.update([cost[0],cost[1]])
                answer+=cost[2]
                break
    return answer
print(solution(5,[[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]]))
'''
n	costs	return
4	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	4
'''