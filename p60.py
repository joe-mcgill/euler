from helper import isPrime2
import itertools

prime_list=[i for i in range(100000) if isPrime2(i)]
print((prime_list))
def is_pair_prime(x,y):
	if isPrime2(int(str(x)+str(y))) and isPrime2(int(str(y)+str(x))):
		return True
	else:
		return False

def n_prime(prime_list,n):
	for i in range(n):
		for j in range(i+1,n):
			#print(prime_list[j])
			if [prime_list[i],prime_list[j]] not in bad_list:
				if is_pair_prime(prime_list[i],prime_list[j]) !=True:
					return [prime_list[i],prime_list[j]]
			else:
				return False
	return True


def four_prime(prime_list):
	for i in range(4):
		for j in range(i+1,4):
			#print(prime_list[j])
			if [prime_list[i],prime_list[j]] not in bad_list:
				if is_pair_prime(prime_list[i],prime_list[j]) !=True:
					return [prime_list[i],prime_list[j]]
			else:
                global bad_list.append(
				return False
	return True
bad_list=[]
good_list=[]

newN=9
flag=0

while flag==0:





print(len(list(itertools.combinations(prime_list,5))))
'''
for n in range(2**len(prime_list)):
	if n%100000==0: print(n)
	tlist=[i for i in str(bin(n)[2:].zfill(len(prime_list)))]
	if sum(map(int,tlist))==4:
		bin_list.append(tlist)
		#print(bin_list)

for i in range(len(prime_list)-3):
	for j in range(i+1,len(prime_list)-2):
		for k in range(j+1,len(prime_list)-1):
			for l in range(k+1,len(prime_list)):
				#print('%d,%d,%d,%d'%(i,j,k,l))
				tlist=['1' if x in [i,j,k,l] else '0' for x in range(len(prime_list))]
				#print(tlist)
				bin_list.append(tlist)
print(bin_list)

prime_combos=itertools.combinations(prime_list,4)
#print(len(list(prime_combos)))
for c in tqdm(prime_combos,total=   len(list(prime_combos))):
	#pl=[prime_list[n] for n in range(len(bin_list[i])) if bin_list[i][n]=='1' ]
	ans=five_prime(c)
	if isinstance(ans,int)==False:
		bad_list.append(ans)
	print(bad_list)
	if ans: 
		print('%s\t%d'%(','.join(c),sum(c)))

prime_combos2=itertools.combinations(prime_list,2)
ct=0
plist=[]
for i in prime_combos2:
	if is_pair_prime(i[0],i[1]):
		good_list.append(i)
	else:
		bad_list.append(i)


print(len(good_list))
print(len(bad_list))

for i in prime_list:
	switch=0
	for j in prime_list:
		if j!=i:
			if is_pair_prime(i,j):
				switch=1
		if switch==0:
			if i in prime_list:
				prime_list.remove(i)

print(len(prime_list))




comb5=itertools.combinations(prime_list,5)

new_comb=[]
for i in list(comb5)[0]:
	for j in good_list:
		if j[0] and j[1] in i:
			pass
		else:
			break
	new_comb.append(i)
	print(i)

print(*(new_comb))
'''
