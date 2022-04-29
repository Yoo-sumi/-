def solution(s):
    q=[]
    for i in s:
        if i in '(':
            if q:
                if q[-1]==')':
                    return False
            q.append(i)
        else:
            if not q:
                return False
            if q[-1]=='(':
                q.pop()
            else:
                q.append(i)
    if q:
        return False

    return True