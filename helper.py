from math import sqrt

def isPrime(x):
    for i in range(2,int(sqrt(x))+1):
        if x%i!=0: pass
        else: return False
    return True
    
for j in range(2,37):
        print('%d\t%s'%(j,isPrime(j)))
	
