result=[]
def hanoi(n,start,end,mid):
    global result
    if n==1:
        result.append([start,end])
    else:
        hanoi(n-1, start, mid, end)
        result.append([start, end])
        hanoi(n-1, mid, end, start)

def solution(n):
    global result
    hanoi(n,1,3,2)
    return result