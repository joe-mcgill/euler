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
										
										
											
										perm_list.append(''.join(temp))
										#numbers=fixed_numbers[:]
										#print(numbers)

divs=[2,3,5,7,11,13,17]

pand=0
for i in perm_list:
	#print(i)
	loop_break=0

	for j in range(1,8):
		if int(i[j:(j+3)])%divs[j-1]!=0:
			loop_break=1
	if loop_break==0:
		pand+=int(i)
		print(pand)
print(pand)
