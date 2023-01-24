# cook your dish here
N = int(input())
for i in range (N):
    n, k = map(int, input().split())
    s = list(map(int, input().strip().split()))
    mex = []
    maxm = int(max(s))
    for i in range(maxm+k+10):
        if k > -1:
            if i not in s:
                mex.append(i)
                k -= 1
    print(mex)
    if(len(mex)>0):
        print(max(mex))
        
    else:
        for i in range(maxm+k+2):
            if k >= -1:
                if i not in s:
                    mex.append(i)
                    k -= 1
        print(max(mex))
