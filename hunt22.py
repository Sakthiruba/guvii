a9=int(input())
value=list(map(int,input().split()))
x1=0
for i in range(a9):
    if sum(value[:i])==sum(value[i+1:]):
        x1=x1+1
if x1>0:
    print("yes")
else:
    print("no")
