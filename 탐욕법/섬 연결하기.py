def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    print(costs)
    connect = set([costs[0][0]])
    while len(connect)!=n:
        for cost in costs:
            if cost[0] in connect and cost[1] in connect:
                continue
            if cost[0] in connect or cost[1] in connect:
                connect.update([cost[0],cost[1]])
                print(connect)
                answer+=cost[2]
                break

    return answer

print(solution(5,[[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]]))
'''
n	costs	return
4	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	4
입출력 예 설명
'''