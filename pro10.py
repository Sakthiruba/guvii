a3=int(input())
b3=[int(i) for i in input().split()]
xxx=0
for i in range(a3):
   for j in range(i):
      if b3[j]<b3[i]:
         xxx+=b3[j]
print(xxx)
