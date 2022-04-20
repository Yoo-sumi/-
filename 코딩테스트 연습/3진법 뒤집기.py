def solution(n):
    answer = 0
    s=""
    while n>2: # 3진법이기 때문에 0,1,2 가 나옴
        a,b=divmod(n,3)
        s+=str(b)
        n=a
    s+=str(n)
    print(s)
    for i in range(len(s)):
        answer+=int(s[-(i+1)])*pow(3,i)
    return answer