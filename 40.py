res=''
for addthis in range(0,250000):
	res+=str(addthis)
print(len(res))

nl=[int(res[i]) for i in range(len(res))]

print((nl[1]*nl[10]*nl[100]*nl[1000]*nl[10000]*nl[100000]*nl[1000000]))

