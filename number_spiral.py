t = int(input())
tab=[]
for i in range(t):
    l = list(map(int, input().split()))
    y = l[0]
    x = l[1]
    if y % 2 == 0 and x <= y:
        chiffre = y ** 2 - x + 1
    elif y % 2 != 0 and x <= y:
        chiffre = (y-1) ** 2 + x
    elif x % 2 != 0 and y <= x:
        chiffre = x ** 2 - y + 1
    elif x % 2 == 0 and y <= x:
        chiffre = (x-1) ** 2 + y
    else:
        exit()
    tab.append(chiffre)

for i in range(len(tab)):
    print(tab[i])