from math import sqrt as rc
nb = int(input("Number to decompose: "))
nbentier = []
result = []

while nb != 1:
	nbentier.append(nb)
	premier = False

	a = 2
	while not premier:
		if nb % a == 0:
			nb = nb / a
			result.append(int(a))
			premier = True
		else:
			a += 1

print(result)
print(nbentier)
