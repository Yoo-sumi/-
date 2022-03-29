def solution(genres, plays):
    answer=[]
    total={}
    index={}
    for i in range(len(genres)):
        total[genres[i]]=total.get(genres[i],0)+plays[i]
        index[genres[i]]=index.get(genres[i],[])+[i]
    max_array=[]
    for i in total.keys():
        max_array.append((total[i],i))
    max_array.sort(reverse=True)
    for i in max_array:
        array=[]
        index_array=index[i[1]]
        for j in index_array:
            array.append((plays[j],j))
        array.sort(key=lambda x:(-x[0],x[1]))
        for j in range(len(array)):
            if j==2:
                break
            answer.append(array[j][1])
    return answer
print(solution(["classic", "pop", "classic", "pop", "classic", "classic"],[400, 600, 150, 600, 500, 500]))