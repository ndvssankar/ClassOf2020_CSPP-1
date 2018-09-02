from itertools import permutations
n=int(input())
lst = []
for i in range(0, n+1):
	lst.append(chr(i+48))
l = list(permutations(lst))
sum = 0
primes = [2,3,5,7,11,13,17]
for i in l:
	string = ''.join(i)
	flag = False
	for j in range(1, len(string)-2):
		prime = primes[j-1]
		if int(string[j:j+3])%prime == 0:
			flag = True
		else:
			flag = False
			break
	if flag:
		sum = sum + int(string)
print(sum)
