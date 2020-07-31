from isPrime2 import isPrime2
import math
from tqdm import tqdm
topnum=100001

#primes=[i for i in range(topnum) if isPrime2(i)]
composites=[ i for i in range(2,topnum) if isPrime2(i)==False and i%2==1]
print('c')
squares=[i**2 for i in range(int(math.sqrt(topnum)+1))]
print('s')

ans=[]
for i in tqdm(composites):
	loop_break=0
	for j in squares:
		if 2*j<i:
			
			if isPrime2(i-(2*j)):
				
				loop_break=1
				break 
	if loop_break==0: ans.append(i)
	
print((ans))
