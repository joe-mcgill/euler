ones=['','one','two','three','four','five','six','seven','eight','nine']
teens=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens=['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

summ=0

def count(x):
	#print(x)
	if x==1000: return('onethousand')
	x=[i for i in str(x)]
	
	if len(x)==1:
		return ones[int(x[0])]
	elif len(x)==2:
		if x[0]=='1':
			return teens[int(x[1])]
		else:
			return tens[int(x[0])]+''+count(x[1])
	elif len(x)==3:
		if int(x[1])+int(x[2])>0:	
			return ones[int(x[0])]+'hundredand'+count(''.join(x[1:]))
		else:
			return ones[int(x[0])]+'hundred'+count(''.join(x[1:]))
for i in range(1,1001):
	print(count(i))
	summ+=len(count(i))

print(summ)
