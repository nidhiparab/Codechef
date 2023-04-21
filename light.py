t = int(input())
for ti in range (t):
    m, r, n = list(map(int,input().split()))
    s = list(map(int,input().split()))
    l=[]
    no=0
    final=0
    for i in range (n):
        q=[]
        start = max(0,s[i]-r)
        end = min(m, s[i]+r)
        for j in range(start,end+1):
            q.append(j) 
        l.append(q)
    
    for i in range (n-1):
        if l[i+1][0] in l[i]:
            y=1
        else:
            no=1
    for i in range (n-1):
        # print(l[i][-1:][0])
        if l[i][-1:][0] == m:
            final = i
            break
    if no == 0:
        print("Case #{}: {}".format(ti+1, "IMPOSSIBLE"))
    else:
        print("Case #{}: {}".format(ti+1, final+1))