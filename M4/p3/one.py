iteration = 0
while iteration < 5:
    count = 0
    for char in "Hello, World":
        count = count + 1
        if iteration % 2 == 0:
            pass
        else:
            break
    print(count)
    iteration+=1
#----------------------------

# i = 1
# sum=0
# while i <= 10:
#     sum = sum + i
# i = i+1
# print(sum)

#----------------------------

for i in range(10):
    if i%2:
        print(i*2)

st = "deepak"
if st[2:4:1] != 'ep' or st[::-1] == 'kaped' or st[::] == "deepak":
    if st[-1:-3:-1] == "ka":
        print(st[-1:-5:-1])