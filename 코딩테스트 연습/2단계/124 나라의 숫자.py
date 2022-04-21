def solution(n):
    result=""
    s=""
    while not 1<=n<=3:
        if n%3==0:
            a,b=divmod(n-1,3)
            s+=str(n-(a*3))
        else:
            a,b=divmod(n,3)
            s+=str(b)
        n=a
    s+=str(n)
    for i in s[::-1]:
        if i=='3':
            i='4'
        result+=i
    return result