nu3=input()
m7= 0
for i in range(0,len(nu3)-1):
  for j in range(i+1,len(nu3)):
    le=nu3[i:j+1]
    if le==le[::-1]:
      if len(le) > m7:
        m7 = len(le)
        k=le
print(k)
