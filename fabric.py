for ti in range (int(input())):
    c=[]
    d=[]
    u=[]
    d1=[]
    c1=[]
    u1=[]
    count=0
    z=int(input())

    for _ in range (z):
        s = list(input().split())
        c.append(s[0])
        d.append(int(s[1]))
        u.append(int(s[2]))

    c1=sorted(c)
    d1=sorted(d)
    u1=sorted(u)

    for j in range(z):
        if (c[j] == c1[j] or d[j]== d1[j]) and u[j] == u1[j]:
            count = count+1
    print("Case #{}: {}".format(ti+1, count))



