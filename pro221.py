a111 = int(input())
a222 = list(map(int, input().split()))
a33 = int(len(a222)/2)
if sum(a222[:a33])//len(a222[:a33]) == sum(a222[a33:])//len(a222[a33:]):
    print('yes')
else:
    print('no')
