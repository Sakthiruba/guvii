st4,st5= input().split()
for i in range(0,len(st4)-len(st5)+1):
  if st4[i:len(st5)+i] == st5:
    print('yes')
    break
else:
  print('no')
