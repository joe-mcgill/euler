import math

fs={}


for i in range(1,10):
	fs[i]=math.factorial(i)

summ=0
n=3
ans=[]
while True:
	if n%1001==0:
		print('%d\t%d'%(n,sum([math.factorial(int(i)) for i in [j for j in str(n)]])))
	if n==sum([math.factorial(int(i)) for i in [j for j in str(n)]]):
		summ+=n
		print('%s\t%d'%(n,summ))
	n+=1