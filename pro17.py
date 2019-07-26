ccom,ddom=map(int,input().split())
l=list(map(int,input().split()))
p=0
for i in range(0,ccom):
    for j in range(1,ccom):
        if l[i]+l[j]==ddom and i!=j:
            p=1
            break
print("yes" if p else "no")
