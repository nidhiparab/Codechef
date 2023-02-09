t=int(input())
for _ in range(t):
    n,x,y=list(map(int,input().split()))
    if n>=(x+2*y):
        print('YES')
    else:
        print('NO')