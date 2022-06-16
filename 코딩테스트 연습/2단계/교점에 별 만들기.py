def contact_point(a,b):
    x1,y1,z1=a
    x2,y2,z2=b
    if x1*y2-y1*x2==0:
        return None
    x=(y1*z2-z1*y2)/(x1*y2-x2*y1)
    y=(z1*x2-z2*x1)/(x1*y2-x2*y1)
    if x==int(x) and y==int(y):
        return (int(x),int(y))
    return None
def solution(line):
    answer = set()
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            point=contact_point(line[i],line[j])
            if point:
                answer.add(point)
    xs=[p[0] for p in answer]
    min_x=min(xs)
    max_x=max(xs)
    ys=[p[1] for p in answer]
    min_y=min(ys)
    max_y=max(ys)
    arr=[['.']*(abs(max_x-min_x)+1) for _ in range(abs(max_y-min_y)+1)]
    for a,b in answer:
        arr[max_y-b][a-min_x]='*'
    for i in range(len(arr)):
        arr[i]="".join(arr[i])
    return arr