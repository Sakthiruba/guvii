wt,pot=input().split()
r12=abs(len(pot)-len(wt))
for k11 in range(len(wt)):
  if(len(pot)==1 and pot[k11] in wt):
    break
  if(wt[k11]!=pot[k11]):
    r12=r12+1
print(r12)
