def solution(m, n, board):
    index=[m]*n
    total=sum(index)
    array=[[] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            array[i].append(board[m-1-j][i])
    while True:
        store2=[[] for _ in range(n)]
        for i in range(n-1):
            for j in range(index[i]-1):
                if j>=index[i+1]-1:
                    continue
                if array[i][j]==array[i][j+1]==array[i+1][j]==array[i+1][j+1]:
                    if not j in store2[i]:
                        store2[i]+=[j]
                    if not j+1 in store2[i]:
                        store2[i]+=[j+1]
                    if not j in store2[i+1]:
                        store2[i+1]+=[j]
                    if not j+1 in store2[i+1]:
                        store2[i+1]+=[j+1]
        stop=True
        for i in store2:
            if len(i)!=0:
                stop=False
        if stop:
            break

        for i in range(len(store2)):
            temp=[]
            for j in range(index[i]):
                if not j in store2[i]:
                    temp.append(array[i][j])
            array[i]=temp
            index[i]=len(array[i])
    return total-sum(index)