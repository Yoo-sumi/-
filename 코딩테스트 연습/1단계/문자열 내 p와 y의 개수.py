def solution(s):
    s=s.lower()
    answer=0
    for i in s:
        if i=='p':
            answer+=1
        elif i=='y':
            answer-=1
    if answer!=0:
        return False
    return True