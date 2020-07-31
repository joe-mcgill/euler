ans=[]

for a in range(1,10001):
	print(a)
	for b in range(1,10001):
		c=a*b
		if len(set(str(a)+str(b)+str(c)))==9 and len(str(a)+str(b)+str(c))==9 and c not in ans and '0' not in set(str(a)+str(b)+str(c)):
			ans.append(c)
			print((str(a)+str(b)+str(c)))
			print ('%d\t%d\t%d'%(a,b,c))		
print(ans)
print(sum(ans))