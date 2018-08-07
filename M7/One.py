l = input().split(" ")
n = int(l[0])
n = n+1
k = int(l[1])
k = k+1
for i in range(2, n):
    flag = False
    l = []
    str1 = sorted(str(i))
    b = i * 2
    str2 = sorted(str(b))
    l.append(i)
    l.append(b)
    if len(str1) == len(str2) and str1 == str2:
        flag = True
        for j in range(3, k):
            c = i * j
            str3 = sorted(str(c))
            if len(str3) == len(str1) and str3 == str1:
                l.append(c)
            else:
                flag = False
                break
    if flag:
        for val in l:
            print(val, end=" ")
        print()

