for ti in range(int(input())):
    s= input()
    f = input()
    count = 0
    for i in s:
        x=ord(f)
        y=ord(i)
        if x<y:
            count = count + (y-x)
        elif x>y:
            count = count + (y+x)
    print("Case #{}: {}".format(ti+1, count))

