a111 = int(input())
a222 = list(map(int, input().split()))
a333 = int(len(a222)/2)
if sum(a222[:a333])//len(a222[:a333]) == sum(a222[a333:])//len(a222[a333:]):
    print('yes')
else:
    print('no')
