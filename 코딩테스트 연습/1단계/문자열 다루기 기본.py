def solution(s):
    if len(s)==4 or len(s)==6:
        for i in s:
            if not 48<=ord(i)<=57:
                return False
        return True
    return False