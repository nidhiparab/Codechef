# cook your dish 
l=[]
s=[]
a =int(input())
for i in range (1,a+1):
    l.append(i)
for i in range(a):
    for j in range(1,a):
        if abs(l[i]-l[j]) % (i+1) == 0:
            if l[i] not in s and l[j] not in s:
                s.append(l[j])
            if l[j] not in s:
                s.append(l[i])
print(s)