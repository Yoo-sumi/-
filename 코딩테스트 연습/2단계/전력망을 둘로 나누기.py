def count(graph,n,cut):
    q=[]
    q.append(cut[0])
    flag=[False]*n
    flag[cut[0]]=True
    flag[cut[1]]=True
    c=0
    while q:
        now=q.pop(0)
        c+=1
        for i in graph[now]:
            if not flag[i]:
                q.append(i)
                flag[i]=True
    return c
def solution(n, wires):
    answer = -1
    graph=[[] for _ in range(n)]
    for a,b in wires:
        a,b=a-1,b-1
        graph[a].append(b)
        graph[b].append(a)
    for a,b in wires:
        a,b=a-1,b-1
        if answer==-1:
            answer=abs(count(graph,n,(a,b))-(n-count(graph,n,(a,b))))
        answer=min(answer,abs(count(graph,n,(a,b))-(n-count(graph,n,(a,b)))))
    return answer