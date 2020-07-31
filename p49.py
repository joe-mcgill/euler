from isPrime2 import isPrime2
from tqdm import tqdm

primes = [ i for i in range(1000,10000) if isPrime2(i)]
for a in tqdm(range(len(primes))):
	i=primes[a]
	for b in range(a+1,len(primes)):
		j=primes[b]
		for c in range(b+1,len(primes)):
			k=primes[c]
			if k-j==j-i:
				if sorted([z for z in str(j)])==sorted([y for y in str(k)]):
					if sorted([x for x in str(i)])==sorted([w for w in str(k)]):
								
						print(','.join(map(str,[i,j,k])))	

