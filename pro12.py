a4,b4=map(int,input().split())
lis=list(map(int,input().split()))
l4=[]
for i in range(0,b4):
     u4,v4=map(int,input().split())
     l4.append([u4,v4])
for i in range(b4):
     lower=l4[i][0]
     upper=l4[i][1]
     s4=sum(lis[lower-1:upper])
     print(s4)
