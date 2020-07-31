import math

def dfunc(x):
	returnlist=[1]
	for i in range(2,int(math.sqrt(x))+1):
		if x%i==0:
			returnlist+=[i,x/i]
	return(sum(returnlist))

dvals={i:dfunc(i) for i in range(2,10001)}

amnumbers=[]
for i in range(2,10001):
	print(i)
	a=i
	b=dfunc(a)
	if a!=b and a==dfunc(b):
		amnumbers+=[a,b]
print(sum(set(amnumbers)))


