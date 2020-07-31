from isPrime2 import isPrime2
from itertools import permutations
all_ans=[]
for num in range(2,1000001):
	if isPrime2(num):

		all_perms=[]
		num_list=[d for d in str(num)]
		
		loop_break=0
		perms=[]
		for i in range(len(num_list)):
			if i==0:
				perms.append(''.join(num_list))
			else:
				perms.append(''.join(num_list[(i):])+''.join(num_list[:i]))
		#perms=list((set(perms)	))
		#print(perms)
		for i in perms:
			if isPrime2(int(''.join(i)))==False:
				loop_break=1
			if loop_break:
				break
		else:
			all_ans.append(num)
print(len(all_ans))
		
