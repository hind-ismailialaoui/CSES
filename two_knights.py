

def factorielle(n):##Fonction pour la factorielle
   if n == 0:
      return 1
   else:
      F = 1
      for k in range(2,n+1):
         F = F * k
      return F

n=int(input())


#sur axe des x
nx=n

#sur axe des y
ny=n

#on regarde combien de 2 x 3 il y a
nx = nx % 2
ny = ny % 2

#nombre de 2 = nx , nombre de 3 = ny
nx = nx * 2
ny = ny * 3

#on multiplie les 2
nxy = nx * ny

#on compte le nombre de places interdites
p = nxy / n
p = 4 * p #il y a 4 cotés

print(p)



x =factorielle(n**2)/(factorielle(2)*factorielle((n**2)-2)) - p #- 2 ** p * p #(2**n)

print(x)