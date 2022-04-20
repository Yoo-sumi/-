def solution(n, arr1, arr2):
    answer = []
    map1=[[] for _ in range(n)]
    map2=[[] for _ in range(n)]
    map=[[0]*n for _ in range(n)]
    for i in range(n):
        s=""
        while arr1[i]>1:
            a,b=divmod(arr1[i],2)
            s+=str(b)
            arr1[i]=a
        s+=str(arr1[i])
        s=s[::-1].zfill(n)
        map1[i]+=list(s)
    for i in range(n):
        s=""
        while arr2[i]>1:
            a,b=divmod(arr2[i],2)
            s+=str(b)
            arr2[i]=a
        s+=str(arr2[i])
        s=s[::-1].zfill(n)
        map2[i]+=list(s)
    for i in range(n):
        for j in range(n):
            if map1[i][j]==map2[i][j]=='0':
                map[i][j]=" "
            else:
                map[i][j]="#"
    for i in range(n):
        answer.append("".join(map[i]))
    return answer