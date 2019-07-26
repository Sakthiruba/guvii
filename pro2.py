from itertools import combinations
asa,bsa=map(int,input().split())
csa=len(str(asa))
lst=list(combinations(str(asa),csa-bsa))
lst=sorted(lst)
print(*lst[0],sep='')
