from isPrime2 import isPrime2

max_val=1000000

available=[i for i in range(1,max_val) if isPrime2(i)]
#print(available)
answers=[]
max_num=len(available)
while len(answers)==0:
	print(max_num)
	if sum(available[:max_num])<max_val:
		for i in range(len(available)-max_num+1):
			#print(i)
			templist=available[i:i+max_num]
			summ=sum(templist)
			if isPrime2(summ) and summ<max_val:
				#print(summ)
				#print(len(templist))
				answers.append((summ,len(templist)))
				print(sorted(answers, key=lambda x: x[1],reverse=True))
				break
	max_num-=1