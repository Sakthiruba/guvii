a8=int(input())
c8=list(map(int,input().split()))
x8=[1]*a8
for p in range(a8):
    if p==0:
        if c8[p]>c8[p+1]:
            x8[p]=x8[p]+x8[p+1]
    elif p>0:
        if c8[p]>c7[p-1]:
            x8[p]=x8[p]+x8[p-1]
print(sum(x8))
