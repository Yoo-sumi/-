def solution(x):
    n=list(str(x))
    total=0
    for i in n:
        total+=int(i)
    if x%total==0:
        return True
    return False