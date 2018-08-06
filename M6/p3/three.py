import math

def getPrimes():
    a = {}
    for i in range(0, 500000):
        a[i] = 1
    # for i in range(2, int(math.sqrt(50))):
    for i in range(2, int(math.sqrt(500000))):
        if a[i] == 1:
            for j in range(2*i, 500000, i):
                a[j] = 0

    primes = []
    for i in range(2, 500000):
        if a[i] == 1:
            primes.append(i)
    return primes

primes = getPrimes()
test_cases = int(input())
for i in range(test_cases):
    n = int(input())
    count = 0
    k = 2
    prime = primes[k]
    count = 0
    if n % 2 == 0:
        print(count)
        continue
    while prime < n:
        j = 1
        val = prime+j**2*2
        while val <= n:
            val = prime+(2*j**2)
            if val == n:
                count = count + 1
                break
            j = j + 1
        k = k + 1
        prime = primes[k]
    print(count)