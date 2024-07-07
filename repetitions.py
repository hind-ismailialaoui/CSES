mot = str(input())
l = list(mot)
x_max = 0  # valeur initiale
x = 1

for i in range(1, len(l)):
    if l[i - 1] == l[i]:
        x += 1
    else:
        if x > x_max:
            x_max = x
        x = 1

if x > x_max:
    x_max = x

print(x_max)