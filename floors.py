T = int(input())
for _ in range (T):
    l=list(map(int,input().split()))
    f=[]
    for a in l:
        if a==100:
            f.append(10)
        elif(a<10):
            f.append(1)
        elif(a%10 != 0):
            a=str(a)
            a=int(a[::-1])
            floor=(a%10)+1
            f.append(floor)
        else:
            a=str(a)
            a=int(a[::-1])
            floor=a%10
            f.append(floor)
    print(abs(f[0]-f[1]))

