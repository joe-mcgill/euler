for a in range(10,101):
	for b in range(10,a):
		a2=str(a)
		b2=str(b)
		for i in range(2):
			if a2[i] in b2 and int(a2[1])!=0:
				
				anew=a2[(i+1)%2]
				bnew=b2[(b2.index(a2[i])+1)%2]
				
				if a!=b and float(bnew)!=0 and float(anew)!=0 and(float(a)/b)==(float(anew)/float(bnew)) :
					print('%d/%d\t%s/%s'%(b,a,bnew,anew))
