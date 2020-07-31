from isPrime2 import isPrime2

def test_catmult(x):
	catlist=str(x)
	n=len(catlist)
	for pos in range(1,n+1):
		if catlist.find(str(pos)) < 0 : 
			return False
			break
	return True

i=0
while True:
	i+=1
	if test_catmult(i):
		if isPrime2(i):
			print(i)

