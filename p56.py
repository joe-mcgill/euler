maxnum=0
for a in range(1,100):
	print(a)
	for b in range(1,100):
		num=a**b
		nums=[int(i) for i in str(num)]
		if sum(nums)>maxnum: maxnum=sum(nums)
		print(maxnum)