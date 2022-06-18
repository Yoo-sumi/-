def solution():
    n,w,L=map(int,input().split())
    trucks=list(map(int,input().split()))
    trucks.reverse()
    road=[0]*w
    answer=0
    while road:
        road.pop(0)
        if not trucks:
            answer+=1
            continue
        if sum(road)+trucks[-1]<=L:
            road.append(trucks.pop())
        else:
            road.append(0)
        answer+=1
    return answer
print(solution())