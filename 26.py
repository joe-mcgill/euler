import fractions

lengths={}
for d in range(2,1001):
	rmndrs=[]
	num=10
	#while True:
	div=num%d
	if div==1:
		remndrs=[1]
	#print(div)
	while div not in rmndrs:
		if(div>0):
			rmndrs.append(div)
			
			num=10*num%d
			div=num%d
		else:
			rmndrs.append(0)
			break
	if rmndrs.index(div)>0:
		rmndrs=rmndrs[(rmndrs.index(div)):]
	lengths[d]=len(rmndrs)

k=max(lengths, key=lambda z: lengths[z])
print(k)