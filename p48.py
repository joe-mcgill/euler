def self_pow(x):
	return x**x

print(sum([self_pow(i) for i in range(1,1001)]))