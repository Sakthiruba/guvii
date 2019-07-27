vj6,vk6=map(int,input().split())
l6=list(map(int,input().split()))
vj6=[]
l6.insert(0,0)
for a in range(vk6):
     v6=[]
     sumup=0
     cc,dd=map(int,input().split())
     for b in range(cc,dd+1):         
         sumup^=l6[b]     
     vj6.append(sumup)
for c in vj6:
    print(c)
