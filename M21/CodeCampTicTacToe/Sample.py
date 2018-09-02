m = int(input())
lower_limit = int("1"+(m-1)*"0")
upper_limit = int(m*"9")

cnt = 0
i = lower_limit
while i <= upper_limit:
    flag = True
    for j in range(0, m-2):
        if sum(map(int, str(i)[j:j+3])) > 9:
            flag = False
            break
    if flag:
        cnt += 1
    if i in [901, 9010, 90100, 901000]
    
print(cnt%(10**9+7))