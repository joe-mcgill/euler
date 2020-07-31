from isPrime2 import isPrime2

layers=1
corners=[1]
prime_corners=[False]
num=1
while True:
	for i in range(1,5):
		num+=layers*2
		corners.append(num)
		prime_corners.append(isPrime2(num))
	ratio=sum(prime_corners)/len(corners)
	if layers%100==0:
		print('%d\t%f'%(1+layers*2,ratio))
	if ratio<.1: 
		print('%d\t%f'%(1+layers*2,ratio))
		break
	layers+=1