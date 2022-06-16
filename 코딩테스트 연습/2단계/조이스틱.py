def alph(s):
    s1,s2=ord('A'),ord(s)
    v1=max(s1,s2)-min(s1,s2)
    v2=(min(s1,s2)-65)+(90-max(s1,s2)+1)
    return min(v1,v2)
def solution(name):
    answer = 0
    min_move=len(name)-1
    for i, char in enumerate(name):
        answer += alph(char)
        next = i + 1
        while True:
            if len(name)<=next:
                break
            if name[next]!='A':
                break
            next += 1
        min_move = min(min_move, i + i + len(name) - next,i+2*(len(name)-next))
    answer += min_move
    return answer