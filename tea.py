t=int(input())
for _ in range(t):
    total=1
    c=0
    x,y,z=list(map(int,input().split()))
    while x>y:
        x-=y
        c+=1
    total=c*z+z
    print(total)