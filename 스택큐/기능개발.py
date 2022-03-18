import math
def solution(progresses, speeds):
    answer = []
    days=[]
    for i in range(len(speeds)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
    print(days)
    count=1
    s=days[0]
    for i in range(1,len(days)):
        if s<days[i]:
            answer.append(count)
            count=1
            s=days[i]
        else:
            count+=1
    answer.append(count)
    print(answer)
    return answer
solution([95, 90, 90, 99, 80, 99],[1, 1, 1, 1, 1, 1])
'''
progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
'''
