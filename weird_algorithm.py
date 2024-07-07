from collections import deque

n = int(input())
tab = []
tab.append(n)

while (n != 1):
    if n % 2 == 0:
        newN = int(n / 2)
        tab.append(newN)
        n = newN
    else:
        newN = int(n * 3 + 1)
        tab.append(newN)
        n = newN

print(*tab, sep=' ')
