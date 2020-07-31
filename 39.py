solutions={}

for endsum in range(1001):
	
	temp_solutions=[]
	for a in range(1,endsum):
		for b in range(1,endsum-a):
			c=endsum-a-b
			sides=sorted([a,b,c])
			if sides[2]**2==sides[1]**2+sides[0]**2:
				temp_solutions.append(sides)
	temp2=[]
	for i in temp_solutions:
		if i not in temp2:
			temp2.append(i)

	solutions[endsum]=len(temp2)
	if endsum%10==0: 
		print(str(endsum) +'\t-\t'+str(sorted(solutions,key =lambda x: solutions[x],reverse=True)[0]))