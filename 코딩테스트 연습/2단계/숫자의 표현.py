def solution(n):
    answer = 0
    for i in range(1,n+1):
        total=i
        if total==n:
            flag=True
        else:
            flag=False
            for j in range(i+1,n+1):
                if total==n:
                    flag=True
                    break
                if total>n:
                    break
                total+=j
        if flag:
            answer+=1
    return answer