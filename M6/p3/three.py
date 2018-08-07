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



dic = {}
def calc():
    for i in range(9, 500000, 2):
        count = 0
        k = 0
        prime = primes[k]
        count = 0
        if i in primes:
            continue
        while prime < i:
            j = 1
            val = prime+2*(j**2)
            while val <= i:
                val = prime+(2*(j**2))
                if val == i:
                    count = count + 1
                    break
                j = j + 1
            k = k + 1
            prime = primes[k]
        print(i, count)
        dic[i] = count
        # print(dic)
    return dic

primes = getPrimes()
calc()
test_cases = int(input())
for i in range(test_cases):
    print(dic[int(input())])
