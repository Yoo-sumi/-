def solution(rows, columns, queries):
    answer = []
    array=[[(i*columns+j)+1 for j in range(columns)] for i in range(rows)]
    for i in queries:
        x1,y1,x2,y2=i[0]-1,i[1]-1,i[2]-1,i[3]-1
        temp=[[0]*(y2-y1+1) for _ in range(x2-x1+1)]
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                temp[i-x1][j-y1]=array[i][j]
        result=100001
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                a=array[i][j]
                if i==x1 and j==y1:
                    array[i][j]=temp[i+1-x1][j-y1]
                elif i==x1:
                    array[i][j]=temp[i-x1][j-1-y1]
                elif j==y2:
                    array[i][j]=temp[i-1-x1][j-y1]
                elif i==x2:
                    array[i][j]=temp[i-x1][j+1-y1]
                elif j==y1:
                    array[i][j]=temp[i+1-x1][j-y1]
                b=array[i][j]
                if a!=b:
                    result=min(result,array[i][j])

        answer.append(result)
    print(array)
    return answer