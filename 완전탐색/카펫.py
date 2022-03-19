def solution(brown, yellow):
    answer = []
    total=brown+yellow
    result=[]
    for i in range(1,total+1):
        if total%i==0:
            a=total//i
            b=i
            if a>b:
                if not (a,b) in result:
                    result.append((a,b))
            else:
                if not (b,a) in result:
                    result.append((b,a))
    for x,y in result:
        if (x-2)*(y-2)==yellow:
            return [x,y]
    return answer
print(solution(24,24))
'''
brown	yellow	return
10	2	[4, 3]
8	1	[3, 3]
24	24	[8, 6]
'''