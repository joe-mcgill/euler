a,b,c,d=1,1,3,2
i=1
count=0
while i <1000:
	a,b,c,d=c,d,2*c+a,c+d
	if (len(str(c))>len(str(d))): count+=1
	i+=1

print(count)