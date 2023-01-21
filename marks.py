
for _ in range (t):
    n=int(input())
    ans=0
    if n%3 != 0:
        for i in range(10):
            if (n+i)%3 == 0:
                ans=i
                break
    print(ans)