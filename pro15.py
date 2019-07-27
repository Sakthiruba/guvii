a6=int(input())
n6=list(map(int,input().split()))
l6=[]
for i in n6:
  k=bin(i)
  l6.append(k)
f=sorted(l6)
f.reverse()
for j in f:
  print(int(j,2))
