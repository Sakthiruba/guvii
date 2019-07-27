vj6,vk6=map(int,input().split())
l7=list(map(int,input().split()))
vj6=[]
l7.insert(0,0)
for a in range(vk6):
     v7=[]
     sumup=0
     cc,dd=map(int,input().split())
     for b in range(cc,dd+1):         
         sumup^=l7[b]     
     vj6.append(sumup)
for c in vj6:
    print(c)
