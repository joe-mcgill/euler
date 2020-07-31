def is_pbin(x):
	str10=[i for i in str(x)]
	strbin=[i for i in bin(x).split('b')[1]]
	binval=True
	val10=True
	for i in range(int(len(strbin)/2)):
		if strbin[0]=='0':
			binval=False
		if (strbin[i]==strbin[-(i+1)]):
			pass
		else:
			binval=False
	for i in range(int(len(str10)/2)):
		if str10[0]=='0':
			val10=False
		if (str10[i]==str10[-(i+1)]):
			pass
		else:
			val10=False
	return binval & val10

ct=0
for num in range(1000000):
	if is_pbin(num):
		ct+=num

print(ct)