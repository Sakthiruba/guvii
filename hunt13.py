st3,st4= input().split()
for i in range(0,len(st3)-len(st4)+1):
  if st3[i:len(st4)+i] == st4:
    print('yes')
    break
else:
  print('no')
