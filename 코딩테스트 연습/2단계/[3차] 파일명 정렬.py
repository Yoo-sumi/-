def solution(files):
    answer = []
    array=[]
    for i in range(len(files)):
        flag=False
        str=""
        file=files[i].lower()
        temp=tuple()
        for j in range(len(file)):
            if 48<=ord(file[j])<=57:
                if flag==False:
                    temp+=(str,)
                    str=""
                    flag=True
                str+=file[j]
            else:
                if flag:
                    temp+=(int(str),i)
                    flag=False
                    break
                str+=file[j]
        if flag:
            temp+=(int(str),i)
        array.append(temp)
    array.sort(key=lambda x:(x[0],x[1],x[2]))
    for a,b,c in array:
        answer.append(files[c])
    return answer