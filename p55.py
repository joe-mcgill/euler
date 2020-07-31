def rev_string(x):
	return ''.join([x[-i] for i in range(1,len(x)+1)])

def is_p(x):
	str_x=str(x)
	return str_x==rev_string(str_x)
ans=0
for i in range(10000):
	counter=1
	ti=i
	while counter<51:
		ti=str(ti)
		ti=int(ti)+int(rev_string(ti))
		print('%d\t%d\t%d'%(i,counter,ti))
		if is_p(ti): break
		counter+=1
	if counter >=50:
		ans+=1

print(ans)