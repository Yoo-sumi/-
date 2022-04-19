def solution(board, moves):
    answer = 0
    si=len(board)
    array=[[] for _ in range(si)]
    print(array)
    for i in range(si):
        for j in range(si):
            if board[si-1-j][i]!=0:
                array[i].append(board[si-1-j][i])
    print(array)
    bucket=[]

    for i in moves:
        if len(bucket)>0:
            if not array[i-1]:
                continue
            if bucket[-1]==array[i-1][-1]:
                bucket.pop()
                answer+=2
                array[i-1].pop()
                continue
        if array[i-1]:
            bucket.append(array[i-1].pop())
    return answer