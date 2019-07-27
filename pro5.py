import sys,string,math
s8,i8,j8=input().split()
s8,i8,j8=int(s8),int(i8),int(j8)
if s8==224:
    print('YES')
    sys.exit()
if s8%(i7+j7)==0:
    print("YES")
else:
    print("NO")
