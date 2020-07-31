def test_catmult(x):
	catlist=''
	for s in x:
		catlist+=str(s)
	
	for pos in range(1,10):
		if catlist.find(str(pos)) < 0 or len(catlist)!=9: 
			return False
			break
	return True

def catmult(x):
	for n in range(2,10):
		strlist=[]
		for m in range(1,n+1):
			strlist.append(str(m*x))
		if test_catmult(strlist):
			print(''.join(strlist))

final_list=[catmult(i) for i in range(100000000)]

