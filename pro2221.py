a1111 = int(input())
a2222 = list(map(int, input().split()))
a3333 = int(len(a2222)/2)
if sum(a2222[:a3333])//len(a2222[:a3333]) == sum(a2222[a3333:])//len(a2222[a3333:]):
    print('yes')
else:
    print('no')
