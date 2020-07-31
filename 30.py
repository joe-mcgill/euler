
summ=0
pow=5
n=1634



n=2
while True:
	
	l=map(int,str(n))
	l=[i**pow for i in l]
	if sum(l)==n:
		summ+=n
		print(summ)
	n+=1
