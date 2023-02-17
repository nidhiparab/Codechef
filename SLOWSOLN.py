for _ in range(int(input())):
    t,n,s = list(map(int,input().split()))
    count= 0
    summ = 0
    ans=[]
    while summ<=s and t!=0:
        if summ + n>s:
            ans.append(s-summ)
        else:
            ans.append(n)
        summ = summ+n
        t =t-1
    for i in ans:
        count = i**2+count
    print(count)
    
    