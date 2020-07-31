from isPrime2 import isPrime2
from tqdm import tqdm
from math import sqrt
num=1
nums=[]
plim=4
while True:
	tempnum=num
	if num%100==0: 
		print(tempnum)
		#print(nums)
	prime_factors=[]
	for i in range(2,int(sqrt(num)+1)+1):
		#print(i)
		if isPrime2(i) and float(tempnum/i).is_integer():
			prime_factors.append(i)
		#	print(prime_factors)
			while(float(tempnum/i).is_integer()):
				tempnum=tempnum/i
		#		print(tempnum)
			if isPrime2(tempnum):
				prime_factors.append(tempnum)
				break
	if len(prime_factors)==plim:
		#print('\n%d\t%s'%(num,','.join(map(str,prime_factors))))
		nums.append(num)
		nums=nums[-plim:]
		#print(nums)
		run=[]
		for j in range(plim)[0:]:
			run.append(num-j)
		
		runsum=0
		for k in run:
			#print(k)
			runsum+=(int(k in nums))
		#print(runsum)
		if runsum==plim: 
			print('\n%d'%(num-plim+1))
			break
	num+=1


#print(nums)
'''
for i in nums:
	run=[i]
	for j in range(plim)[1:]:
		run.append(i+j)
	runsum=0
	for k in run:
		runsum+=(int(k in nums))
	if runsum==plim: print(i)
'''