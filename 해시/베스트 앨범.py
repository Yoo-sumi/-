def solution(genres, plays):
    answer = []
    dic_sum={}
    dic_index={}
    for i in range(len(plays)):
        dic_sum[genres[i]]=dic_sum.get(genres[i],0)+plays[i]
        dic_index[genres[i]]=dic_index.get(genres[i],[])+[i]
    a=[]
    for i in dic_sum.keys():
        a.append((dic_sum[i],i))
    a.sort(reverse=True)
    print(a)
    for i in range(len(a)):
        genre=a[i][1]
        indexs=dic_index[genre]
        b=[]
        if len(indexs)==1:
            answer.append((indexs[0]))
            continue
        for j in indexs:
            b.append((plays[j],j))
        b.sort(key=lambda x:(-x[0],x[1]))
        answer.append(b[0][1])
        answer.append(b[1][1])
    print(answer)
    #a=sorted(a,key=lambda x: (-x[0],x[1]))
    return answer

solution(["classic", "pop", "classic", "classic"],[500, 600, 150, 800])
'''genres	plays	return
["classic", "pop", "classic", "classic", "pop"]	
[500, 600, 150, 800, 2500]	
[4, 1, 3, 0]'''