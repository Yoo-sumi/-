def solution(n, left, right):
    answer = []
    left_x,left_y=left//n,left%n
    right_x,right_y=right//n,right%n
    i,j=left_x,left_y
    while True:
        if j==n:
            i+=1
            j=0
            continue
        answer.append(max(i,j)+1)
        if (right_x,right_y)==(i,j):
            break
        j+=1
    return answer