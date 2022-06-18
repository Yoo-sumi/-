def same_id(id1,id2):
    if len(id1)!=len(id2):
        return False
    for i in range(len(id1)):
        if id1[i]=='*' or id2[i]=='*':
            continue
        if id1[i]!=id2[i]:
            return False
    return True
def solution(user_id, banned_id):
    answer = []
    q=[]
    index=0
    id=banned_id[index]
    for i in user_id:
        if same_id(i,id):
            q.append(([i],index+1))
    while q:
        id_arr,index=q.pop(0)
        if index==len(banned_id):
            id_arr.sort()
            if not id_arr in answer:
                answer.append(id_arr)
            continue
        id=banned_id[index]
        for i in user_id:
            if i in id_arr:
                continue
            if same_id(i,id):
                q.append((id_arr+[i],index+1))
    return len(answer)