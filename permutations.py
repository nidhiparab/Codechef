from itertools import permutations
from statistics import median
n=int(input())
l=[]
m=[]
chk=True
for i in range(1,n+1):
    l.append(i)
z=list(permutations(l))
for i in z:
    l=[]
    m=[]
    for j in range(len(i)):
        l.append(i[j])
        m.append(int(median(l)))
    for x in m:
        if x != m[0]:
           chk=False
           break;
    if (chk == True):
        print(m)
        break
print(i) 