def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge=[0]*bridge_length
    truck_weights.reverse()
    while bridge:
        answer+=1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge)+truck_weights[-1]<=weight:
                bridge.append(truck_weights.pop())
            else:
                bridge.append(0)
    return answer

print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))
'''
bridge_length	weight	truck_weights	return
2	10	[7,4,5,6]	8
100	100	[10]	101
100	100	[10,10,10,10,10,10,10,10,10,10]	110
'''