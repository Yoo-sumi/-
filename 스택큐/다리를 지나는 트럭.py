def solution(bridge_length, weight, truck_weights):
    answer = 0
    q=[0 for _ in range(bridge_length)]
    truck_weights.reverse()

    while q:
        answer+=1
        q.pop(0)
        if truck_weights:
            if sum(q)+truck_weights[-1]<=weight:
                q.append(truck_weights.pop())
            else:
                q.append(0)
    return answer
print(solution(2,10,[7,4,5,6]))
'''
bridge_length	weight	truck_weights	return
2	10	[7,4,5,6]	8
100	100	[10]	101
100	100	[10,10,10,10,10,10,10,10,10,10]	110
'''