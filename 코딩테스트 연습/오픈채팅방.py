def solution(record):
    result = []
    #0 in 1 out 2 change
    state={"Enter":0,"Leave":1,"Change":2}
    ss={0:"들어왔습니다.",1:"나갔습니다."}
    dic={}
    for i in record:
        li=list(i.split())
        if li[0]=="Enter" or li[0]=="Change":
            dic[li[1]]=li[2]
        if li[0]=="Change":
            continue
        result.append((state[li[0]],li[1]))
    for i in range(len(result)):
        a,b=result[i]
        result[i]="{0}님이 {1}".format(dic[b],ss[a])
    return result
a=[]
a