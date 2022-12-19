t = int(input())
for ti in range (t):
    N,M = list(map(int,input().split()))
    c = list(map(int,input().split()))
    given = sum(c)//M
    remain = sum(c)-(given*M)
    print("Case #{}: {}".format(ti+1, remain))