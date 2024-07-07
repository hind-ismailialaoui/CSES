n = int(input())

tab=[]
if n == 2 or n==3:
    print("NO SOLUTION")
    exit()
for _ in range(1, n+1):
    if _ % 2 ==0:
        tab.append(_)
        _ +=1
for _ in range(1, n+1):
    if _ % 2 != 0:
        tab.append(_)
        _ +=1
print(*tab, sep=' ')