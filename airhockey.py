N = int(input())
for i in range (N):
    x, y = map(int, input().split())
    print(7-max(x,y))