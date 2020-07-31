fixed_numbers=['0','1','2','3','4','5','6','7','8','9']
count=0
perm_list=[]
for i in ['0','1','2','3','4','5','6','7','8','9']:
	numbers=fixed_numbers[:]
	#print(fixed_numbers)
	numbers.remove(i)
	#print(numbers)
	numbers2=numbers[:]
	for j in numbers2:
		#print(j)
		numbers3=numbers2[:]
		numbers3.remove(j)
		#print(numbers2)
		
		for k in numbers3:
			numbers4=numbers3[:]
			numbers4.remove(k)
			for l in numbers4:
				numbers5=numbers4[:]
				numbers5.remove(l)
				for m in numbers5:
					numbers6=numbers5[:]
					numbers6.remove(m)
					
					for n in numbers6:
						numbers7=numbers6[:]
						numbers7.remove(n)
						for o in numbers7:
							numbers8=numbers7[:]
							numbers8.remove(o)
							for p in numbers8:
								numbers9=numbers8[:]
								numbers9.remove(p)
								for q in numbers9:
									numbers10=numbers9[:]
									numbers10.remove(q)
									for r in numbers10:
										temp=[i,j,k,l,m,n,o,p,q,r]
										count+=1
										if count%10000==0:
											print(temp)
											
										perm_list.append(temp)
										#numbers=fixed_numbers[:]
										#print(numbers)
print(sorted([''.join(i) for i in perm_list])[999999])
print(len(perm_list))
print(10*9*8*7*6*5*4*3*2*1)