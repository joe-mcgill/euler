def factorial(x):
	prod=1
	for i in range(2,x+1):
		prod*=i
	return(prod)

def comb(n,r):
	return factorial(n)/(factorial(r)*factorial(n-r))

count=0
'''
for i in range(23,101):
	if i%2==0:
		userange=range(1,int(i/2)+1)
	else:
		userange=range(1,int(i/2)+1)

	for r in userange:
		if comb(i,r)>1000000:
			if r==i/2:
				count+=1
			else:
				count+=2
			#print('%d\t%d'%(i,r))
'''
for i in range(23,101):
	for r in range(1,i+1):
		if comb(i,r)>1000000:
			count+=1#print('%d\t%d'%(i,r))
print(count)