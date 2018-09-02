# fill in this function
def fib():
    a = 0
    b = 1
    yield a
    yield b
    c = a + b
    yield c
    while True:
        a = b
        b = c
        c = a + b
        yield c



# testing code
import types
print(type(fib()))
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")
    lst = []
    counter = 0
    for n in fib():
        print(n)
    #     lst.append(n)
        counter += 1
        if counter == 10:
            break
    # print(lst)