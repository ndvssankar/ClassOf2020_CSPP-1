def triangle_pentagonal(n, a, b):
	tn = [1]
	pn = [1]
	k = 2
	i = 1
	j = 4
	while pn[i-1] <= n:
		tn.append(tn[i-1] + k)
		k = k + 1
		# pn.append((i*(3*i-1))//2)
		pn.append(j + pn[i-1])
		j = j + 3
		i = i + 1
	for i in tn:
		if i in pn:
			print(i)
		

def pentagonal_hexagonal(n, a, b):
	pn = [1, 5]
	hn = [1, 6]
	i = 2
	k = 9
	j = 7

	while hn[i-1] <= n:
		pn.append(j + pn[i-1])
		hn.append(k+hn[i-1])
		print(pn[i], hn[i])
		j = j + 3
		k = k + 4
		i = i + 1


	for i in pn:
		if i in hn:
			print(i)

lst = input().split(" ")
n = int(lst[0])
a = int(lst[1])
b = int(lst[2])
if a == 3 and b == 5:
	triangle_pentagonal(n, a, b)
else:
	pentagonal_hexagonal(n, a, b)
	