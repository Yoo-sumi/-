def solution(s):
    li=s.split(' ')
    maxx=-1e9
    minn=1e9
    for i in li:
        maxx=max(maxx,int(i))
        minn=min(minn,int(i))
    return str(minn)+" "+str(maxx)