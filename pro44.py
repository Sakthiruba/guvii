ar,br,cr,d = map(int, input().split())
xiii = list(map(int, input().split()))
zzzz = []
i = 0
for i in range(0, len(xiii)):
    for j in range(i, len(xiii)):
        for k in range(j, len(xiii)):
            zzzz.append(sum((br*xiii[i], cr*xiii[j], d*xiii[k])))
print(max(zzzz))
