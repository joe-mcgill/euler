fib=[1,1]
start=2
print('Fib 1:\t1\nFib 2:\t1')
i=3
while (len(str(fib[-1]))<3):
#for i in range(10):
	fib.append(fib[-1]+fib[-2])
	print('Fib %d:\t%d'%(i,fib[-1]))

	i+=1
