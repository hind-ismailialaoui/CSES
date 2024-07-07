n = int(input())

l = list(map(int, input().split()))
sum = 0

for x in l:
    sum += x

print(int(n * (n + 1) / 2 - sum))
