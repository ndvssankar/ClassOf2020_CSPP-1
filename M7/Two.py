def getPrimes():
	a = {}
	for i in range(0, 1000):
		a[i] = 1
	# for i in range(2, int(math.sqrt(50))):
	for i in range(2, int(math.sqrt(1000))):
	    if a[i] == 1:
	        for j in range(2*i, 1000, i):
	            a[j] = 0

	primes = []
	for i in range(2, 1000):
	    if a[i] == 1:
	        primes.append(i)

	return primes

primes = getPrimes()

test_cases = int(input())
for i in range(test_cases):
	n = int(input())
	count = 0
	res = 0
	for j in primes:
		res = res + j
		if res - n in primes:
			count += 1





