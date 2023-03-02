for ti in range (int(input())):  
    count = 1
    N = int(input())
    l = [1]
    for j in range(1,N):
        l.append(0)
    for i in range(1,len(l)):
        if count == 1:
            if i == len(l)-1:
                if l[i-1] == 0 and l[i-2]==0:
                    l[i]=2
                    count = 0
            else:
                if l[i-1] == 0 and l[i+1]==0 and l[i-2]==0:
                    l[i]=2
                    count = 0
        else:
            if i == len(l)-1:
                if l[i-1] == 0:
                    l[i]=1
                    count = 1
            else:
                if l[i-1] == 0 and l[i+1]==0:
                    l[i]=1
                    count = 1
    print("Case #{}: {}".format(ti+1, l.count(1)))
