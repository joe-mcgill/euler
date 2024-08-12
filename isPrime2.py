def isPrime2(n):
	if n==2 or n==3: return True
	if n%2==0 or n<2: return False
	for i in range(3,int(n**0.5)+1,2):
		if n%i==0:
			return False 

	return True

def primeFactors(x):
    primeFactors=[]
    tempx=x
    factor=2
    while tempx!=1:
        if isPrime2(factor):
            if tempx%factor==0: primeFactors.append(factor)
            while tempx%factor==0:
                tempx=tempx/factor
        factor+=1
    return primeFactors

def isPalindrome(x):
    x=str(x)[:]
    x2=x.reverse()
    print(x)
    print(x2)
    tv=''.join(x)==''.join(x2)
    return tv
