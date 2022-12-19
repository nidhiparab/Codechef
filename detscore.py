T = int(input())
for _ in range (T):
    x,n= map(int,input().split())
    score=x/10
    total=score*n
    print(int(total))