def solution(n,a,b):
    result=[i+1 for i in range(n)]
    count=0
    while True:
        count+=1
        answer=[]
        for i in range(0,len(result),2):
            x,y=result[i],result[i+1]
            if x in [a,b] and y in [a,b]:
                return count
            if x in [a,b]:
                answer.append(x)
            elif y in [a,b]:
                answer.append(y)
            else:
                answer.append(min(x,y))
        result=answer.copy()
    return answer