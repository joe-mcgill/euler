num=1
loop_break=0
while loop_break==0:
	sort1=sorted([i for i in str(num)])
	sort2=sorted([i for i in str(num*2)])
	if sort2==sort1:
		sort3=sorted([i for i in str(num*3)])
		if sort3==sort1:
			sort4=sorted([i for i in str(num*4)])
			if sort4==sort1:
				sort5=sorted([i for i in str(num*5)])
				if sort5==sort1:
					sort6=sorted([i for i in str(num*6)])
					if sort6==sort1:
						print(num)
						loop_break=1

	num+=1
