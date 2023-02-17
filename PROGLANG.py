from itertools import islice
for _ in range(int(input())):
    count1=0
    count2=0
    a = list(map(int,input().split()))
    ans = iter(a)
    out = [list(islice(ans,2)) for i in range(3)]
    for i in out[0]:
        if i in out[1]:
            count1 = count1 +1
        if i in out[2]:
            count2 = count2 +1
    if count1>count2:
        print("1")
    elif count1<count2:
        print("2")
    else:
        print("0")
        
    