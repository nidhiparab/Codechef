n,q=map(int,input().split())
container = [1]
count = 0
tank=[1]
i=0
x=0
zz=0
for _ in range(1,n):
    k=i
    i,j = map(int,input().split())
    if k==i:
        z=tank.pop()
        tank.append(z+1)
    else:
        tank.append(1)
    container.append([i,j])
for i in tank:
    while i>0 and q>0:
        i=i-1
        q=q-1
    if i==0:
        zz=zz+1
print(tank)
        

