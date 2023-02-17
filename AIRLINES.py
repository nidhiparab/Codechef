for _ in range(int(input())):
    x,y,z=list(map(int, input().split()))
    cost=0
    x=x*10
    if y>x:
        print(x*z)
    else:
        print(y*z)
        
