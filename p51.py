from isPrime2 import isPrime2
from tqdm import tqdm

ans_primes=[i for i in range(1000000) if isPrime2(i)]
all_primes=[i for i in ans_primes if str(i).count('0')==3 or str(i).count('1')==3 or str(i).count('2')==3]

#print(len(all_primes))
#all_primes=[i for i in all_primes if isPrime2(i)]



go=True

prime_numbers=8
loop_break=0
for pnum in ans_primes:
	#print(pnum)
	if loop_break==0:
		strnum=str(pnum)
		#if num%10000==0: print(num)
		for i in range(0,len(strnum)-2):
			#print(i)
			for j in range(i+1,len(strnum)-1):
				for k in range(j+1,len(strnum)):
					count=0
					if i==0:
						digrange=range(1,10)
					else: 
						digrange=range(10)
					
					for digit in map(str,digrange):

							templst=[digit if (a==i or a==j or a==k) else strnum[a] for a in range(len(strnum))]
							tmpnum=int(''.join(templst))
							if isPrime2(tmpnum): 
								count+=1
							#print('%d\t%s\t%d'%(tmpnum,isPrime2(tmpnum),count))
					if count==prime_numbers:
						count=1
						print('\n'+strnum+'\t'+str(count)+'\n')
						loop_break=1
				
						for digit in map(str,digrange):

								templst=[digit if (a==i or a==j or a==k) else strnum[a] for a in range(len(strnum))]
								tmpnum=int(''.join(templst))
								if isPrime2(tmpnum): 
									count+=1
								print('%d\t%s\t%d'%(tmpnum,isPrime2(tmpnum),count))
