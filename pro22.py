ammm=int(input())
arrr=list(map(int,input().split()))
arrr.sort(reverse=True)
s00=0
s1=0
res=[]
for i in range(0,ammm,2):
    s00=s00+arr[i]
for j in range(1,ammm,2):
    s1=s1+arrr[j]
res.append([s00,s1])
for i in res:
    print(i[0] if i[0]>i[1] else i[1])
