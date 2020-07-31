x=100

l=[]
for a in range(2,x+1):
	for b in range(2,x+1):
		l.append(a**b)

print(len(set(l)))