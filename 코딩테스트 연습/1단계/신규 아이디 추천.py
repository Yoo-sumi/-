def solution(new_id):
    answer = ''
    #1
    new_id=new_id.lower()
    #2 a=97, z=122, 0=48, 9=57
    s=""
    for i in new_id:
        if not 97<=ord(i)<=122 and not 48<=ord(i)<=57 and not i in ['-','_','.']:
            continue
        s+=''.join(i)
    new_id=s
    #3
    s=new_id[0]
    for i in range(1,len(new_id)):
        if s[-1]==new_id[i]=='.':
            continue
        s+=''.join(new_id[i])

    #4
    if len(s)>0:
        if s[0]=='.':
            s=s[1:]
    if len(s)>0:
        if s[-1]=='.':
            s=s[:-1]
    #5
    if s=="":
        s+='a'
    #6
    if len(s)>=16:
        s=s[:15]
        if s[-1]=='.':
            s=s[:-1]
    #7
    if len(s)<=2:
        while len(s)!=3:
            s+=s[-1]



    return s


print(round(63.5))