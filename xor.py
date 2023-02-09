t=int(input())
for _ in range (t):
    n,a,b=map(int,input().split())
    max3=0
    ans=0
    for i in range (0,2**n):
        if max3 <= (a^i)*(b^i):
            max3 = (a^i)*(b^i)
            ans=i
print(ans)


