from isPrime2 import isPrime2

def trunc_prime_r(x):
	if x<10:
		return 
	
	loop_break=0
	if isPrime2(x)==False:
		loop_break=1 
	for i in range(1,len(str(x))):
		temp=int(str(x)[:-i])
		if isPrime2(temp)==False:
			loop_break=1

		if loop_break==1:
			break
	if loop_break==0:
		return True

def trunc_prime_l(x):
	if x<10:
		return 
	
	loop_break=0
	if isPrime2(x)==False:
		loop_break=1 
	for i in range(1,len(str(x))):
		temp=int(str(x)[i:])
		if isPrime2(temp)==False:
			loop_break=1
		if loop_break==1:
			break
	if loop_break==0:
			return True

for i in range(1):
	print isPrime2(3979)
ct=11
answers=[]
while(len(answers)<11):
	if trunc_prime_l(ct) and trunc_prime_r(ct):
		answers.append(ct)
		print(answers)
	ct+=1

print(sum(answers))