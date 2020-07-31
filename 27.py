from isPrime2 import isPrime2

length={}

for a in range(-1000,1001):
	print(a)
	for b in range(-1000,1001):
		prime_count=0
		n=0
		while True:
			if isPrime2(n**2+a*n+b):
				prime_count+=1
				n+=1
			else:
				break
		length[(a,b)]=prime_count

print(max(length, key=lambda z: length[z]))

