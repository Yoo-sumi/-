def solution(numbers):
    answer = []
    for num in numbers:
        s=""
        if num==0:
            answer.append(1)
            continue
        number=num
        while number>0:
            a=number//2
            b=number%2
            s+=str(b)
            number=a
        s+=str(a)
        s=s[::-1]
        if int(num)%2==0:
            a=s[:-1]+'1'
            aa=0
            for i in range(len(a)):
                aa+=int(a[len(a)-1-i])*(2**i)
            answer.append(aa)
        else:
            s=s.zfill(len(s)+1)
            for i in range(len(s)-1,-1,-1):
                if s[i]=='0':
                    s=s[:i]+'10'+s[i+2:]
                    break
            aa=0
            for i in range(len(s)):
                aa+=int(s[len(s)-1-i])*(2**i)
            answer.append(aa)
    return answer