def solution(m, musicinfos):
    result=[]
    m2=""
    for i in range(len(m)):
        if m[i]=="#":
            continue
        if i+1<len(m):
            if m[i+1]=="#":
                m2+=m[i].lower()
                continue
        m2+=m[i]
    for j in range(len(musicinfos)):
        start,end,name,song=musicinfos[j].split(',')
        hh,mm=start.split(":")
        start=int(hh)*60+int(mm)
        hh,mm=end.split(":")
        end=int(hh)*60+int(mm)
        s=""
        for i in range(len(song)):
            if song[i]=="#":
                continue
            if i+1<len(song):
                if song[i+1]=="#":
                    s+=song[i].lower()
                    continue
            s+=song[i]
        s=s*(end-start)
        song=s[:(end-start)]
        for i in range(len(song)):
            temp=song[i:i+len(m2)]
            if temp==m2:
                result.append((end-start,j,name))
                break
    if not result:
        return "(None)"
    result.sort(key=lambda x:(-x[0],x[1]))
    return result[0][2]