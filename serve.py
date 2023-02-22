T = int(input())
for _ in range (T):
    p,q = map(int, input().split())
    if (p+q == 0):
        print("Alice")
    elif (p+q) % 4 == 0 :
        print("Alice")
    elif (p+q) % 2 == 0 :
        print("Bob")
    elif (p+q+1) % 4 == 0 :
        print("Bob")
    elif (p+q+1)% 2 == 0:
        print("Alice")