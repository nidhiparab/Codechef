n = int(input())
c = list(map(int,input().split()))

score = 0
max = c[0]
ans = [0]
for i in c:
    if i>ans[len(ans)-1]:
        ans.append(i)
    while(min(ans)!=i):
        print(i)
        ans.remove(min(ans))
print(ans)