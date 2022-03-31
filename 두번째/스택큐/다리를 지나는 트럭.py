from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights.reverse()
    q=deque()
    w=0
    w+=truck_weights[-1]
    q.append((truck_weights.pop(),1))
    while truck_weights or q:
        array=[]
        flag=False
        while q:
            now=q.pop()
            if now[1]==bridge_length:
                w-=now[0]
            if w<weight and len(truck_weights)>0 and flag==False:
                if w+truck_weights[-1]<=weight:
                    w+=truck_weights[-1]
                    flag=True
                    array.append((truck_weights.pop(),1))
            if now[1]!=bridge_length:
                array.append((now[0],now[1]+1))
        answer+=1
        for i in array:
            q.append(i)

    return answer+1

print(solution(5,5,[2,2,2,2,1,1,1,1,1]))
'''
bridge_length	weight	truck_weights	return
2	10	[7,4,5,6]	8
100	100	[10]	101
100	100	[10,10,10,10,10,10,10,10,10,10]	110
'''