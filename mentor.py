N =int(input())
l = list(map(int,input().split()))
l.sort()
m = []
for i in l:
    print(i)
    for j in range(N-1, -1, -1):
        if l[j] <= 2*i:
            m.append(l[j])
            break
print(m)