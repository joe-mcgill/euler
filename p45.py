T=[i*(i+1)/2 for i in range(1,100001)]
P=[i*(3*i-1)/2 for i in range(1,100001)]
H=[i*(2*i-1) for i in range(1,100001)]
print(max(P))
print(max(T))
print(max(H))


for i in T:
	if (i in P) and (i in H):
		
		print(i)
	
