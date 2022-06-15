def solution(n, t, m, p):
    answer = ''
    count=0
    total=0
    start_num=0
    flag=True
    while flag:
        num=start_num
        arr=[]
        while num>=n:
            if 10<=num%n<=15:
                arr.append(chr(num%n+55))
            else:
                arr.append(num%n)
            num//=n
        if 10<=num<=15:
            arr.append(chr(num+55))
        else:
            arr.append(num)
        for i in arr[::-1]:
            if count%m==p-1:
                answer+=str(i)
                total+=1
                if total==t:
                    flag=False
                    break
            count+=1
        start_num+=1
    return answer