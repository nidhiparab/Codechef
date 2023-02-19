for _ in range(int(input())):
    n = int(input())
    s = list(map(str,input()))
    last="na"
    i=0
    
    for j in range (s.count(".")):
        s.remove('.')
    # print(s)
    n = len(s)
    for k in range(0,n):
        
        if s[0] == "T":
            print("Invalid")
            i=1
            break
        if s[n-1] == "H":
            print("Invalid")
            i=1
            break
        if last == s[k]:
            print("Invalid")
            i=1
            
            break
        if s[k] == "H" or s[k] == "T":
            last = s[k]
    if i == 0:
        print("Valid")
    
    
