n = int(input())
numerator = [3]
denominator = [2]

for i in range(1, n):
	denominator.append(numerator[i-1] + denominator[i-1])
	numerator.append(denominator[i-1] + denominator[i])
	print(numerator[i], "/", denominator[i])
	if len(str(numerator[i])) > len(str(denominator[i])):
		print(i+1)