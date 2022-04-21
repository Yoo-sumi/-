def solution(s, n):
    answer = ''
    for i in s:
        num=ord(i)
        if 97<=num<=122:
            num+=n
            if num>122:
                answer+=chr(97+(num-123))
            else:
                answer+=chr(num)
        elif 65<=num<=90:
            num+=n
            if num>90:
                answer+=chr(65+(num-91))
            else:
                answer+=chr(num)
        else:
            answer+=i
    return answer