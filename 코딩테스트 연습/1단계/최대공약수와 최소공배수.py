def solution(n, m):
    answer = []
    min_value=min(n,m)
    for i in range(min_value,1,-1):
        if n%i==m%i==0:
            answer+=[i,n/i*m/i*i]
            break
    if len(answer)==0:
        answer+=[1,n*m]
    return answer