lst = input().split(" ")
n = int(lst[0])
k = int(lst[1])
strk = ""
for i in range(1, k+1):
    strk = strk + str(i)
for i in range(2, n+1):
    product = 1
    j = 1
    result = ""
    while len(result) < k:
        product = j * i
        j = j + 1
        result = result + str(product)
    if len(result) == k:
        found = False
        for char in strk:
            if char not in result:
                found = True
        if not found:
            print(i)


