for ti in range (int(input())):
    n=int(input())
    p = input()
    pq="ab"
    q=""
    i=0
    while (pq != pq[::-1] and i<len(p)):
        q = q+p[::-1][i]
        pq = p + q
        i += 1
    print("Case #{}: {}".format(ti+1, q))