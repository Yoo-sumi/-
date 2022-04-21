def solution(s):
    if len(s)%2!=0:
        answer=s[len(s)//2]
    else:
        index=len(s)//2
        answer=s[index-1:index+1]
    return answer