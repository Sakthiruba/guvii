from itertools import combinations
as,bs=map(int,input().split())
cs=len(str(as))
lst=list(combinations(str(as),c-b))
lst=sorted(lst)
print(*lst[0],sep='')
