for _ in range (int(input())):   
    x,y,a = map(int, input().split())
    if a>x or a==x:
        if a<y:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")