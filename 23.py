import math

def dfunc(x):
	returnlist=[1]
	for i in range(2,int(math.sqrt(x))+1):
		if x%i==0:
			returnlist+=[i,x/i]
	return(sum(returnlist))

print(dfunc(28123))

abundantnumber=[i for i in range(12,28123) if dfunc(i)>i]
print(abundantnumber)


abundantsums=[]
for i in abundantnumber:
	for j in abundantnumber:
		abundantsums.append(i+j)

abundantsums=set(abundantsums)
#print(sorted(abundantsums))
notsumm=[no for no in range(24,28124) if no not in abundantsums]
print(notsumm)
print(sum((notsumm)))
