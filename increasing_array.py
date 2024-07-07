n = int(input())
l = list(map(int, input().split()))

nbChangement = 0
for i in range(1, len(l), 1):
    if l[i - 1] > l[i]:
        nbChangement += (l[i - 1] - l[i])
        l[i] = l[i - 1]

print(nbChangement)