def solution(s):
    answer =[]
    result=[]
    s=s[2:-2].split('},{')
    for i in s:
        i=i.split(',')
        answer.append(i)
    answer.sort(key=lambda x:len(x))
    for i in answer:
        for j in i:
            if not int(j) in result:
                result.append(int(j))
    return result