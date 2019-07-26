ar=int(input())
br=0
l=[]
for ar in range(1,ar+1):
  l.append(ar)
for ar in range(len(l)):
  for ar in range(ar+1,len(l)):
    br+=1
print(br)
