import timeit
def power(x):
	return x*x
s = map(power, range(10))
# print(list(s))
# s = [x**2 for x in range(10)]

v = [2**i for i in range(13)]
m = [x for x in s if x % 2 == 0]
# print(v)
# print(m)
# print("============================================================")

s = [x**3 for x in range(10)]
# print(s)
# print("============================================================")

numbers = range(1, 10)
lst = [x**2 for x in numbers if x%2 == 0]
# print(lst)
# print("============================================================")

# Initialize the `kilometer` list 
kilometer = [39.2, 36.5, 37.3, 37.8]

# Construct `feet` with `map()`
feet = map(lambda x: float(3280.8399)*x, kilometer)

feet = [3280.8399*x for x in kilometer]

# Print `feet` as a list 
# print(feet)

# Map the values of `feet` to integers 
feet = list(map(int, feet))

# Filter `feet` to only include uneven distances 
uneven = filter(lambda x: x%2, feet)

# Check the type of `uneven`
# print(type(uneven))

# Print `uneven` as a list
# print(list(uneven))

from functools import reduce
reduce_feet = reduce(lambda x,y: x+y, feet)
# print(reduce_feet)
# print(sum(feet))

# print(timeit.timeit('[n**2 for n in range(10) if n%2==0]', number=10000))

# def power_two(numbers):
# 	new_list = []
# 	for n in numbers:
# 		if n%2==0:
# 			new_list.append(n**2)
# 	return new_list

# # Print the execution time 
# print(timeit.timeit('power_two(numbers)', globals=globals(), number=10000))


x = ["Fizz" if x%2==0 else "Buzz" for x in range(10)]
print(x)

lst = [(x,y,z) for x in range(1,30000) for y in range(x,30000) for z in range(y,30000) if x**2 + y**2 == z**2]
print(lst)

