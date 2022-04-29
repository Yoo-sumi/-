def solution(n):
    answer = n+1
    start=n+1
    count=0
    m=n
    n_str=""
    while m>0:
        a,b=divmod(m,2)
        n_str+=str(b)
        m=a
    n_str+=str(m)
    while True:
        s=""
        while start>0:
            a,b=divmod(start,2)
            s+=str(b)
            start=a
        s+=str(start)
        if s.count('1')==str(n_str).count('1'):
            break
        answer+=1
        start=answer
    return answer