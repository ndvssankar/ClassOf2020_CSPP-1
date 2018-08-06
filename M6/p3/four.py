l = input().split(" ")
n = int(l[0])
k = int(l[1])
lst = []
for j in range(2, n+1, 1):
    flag = False
    str1 = str(j)
    str2 = str(j*2)
    lst = []
    if sorted(str1) == sorted(str2):
        lst.append(str1)
        lst.append(str2)
        flag = True
        for i in range(3, k+1):
            str1 = str(j * i)
            if sorted(str1) == j:
                flag = True
                lst.append(str1)
            else:
                flag = False
                break
        if flag == True:
            for i in lst:
                print(i, end = " ")
            print()
            


