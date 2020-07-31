r=1001

nums=[*range(1,(r*r+1))]
ind=1
sums=1
#print(nums)
for i in range(2,r,2):
	print('*** '+str(i)+' ***')
	for j in range(4):
		ind+=i
		print(ind)
		sums+=ind
#sums+=(r**2-r+1)
print('*****'+str(sums)+'********')