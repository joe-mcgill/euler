import string

text=list(map(int,open('p059_cipher.txt').readlines()[0].split(',')))

for a in range(26):
	x=chr(a+97)
	print(x)
	for b in range(26):
		y=chr(b+97)
		for c in range(26):
			message=[]
			z=chr(c+97)
			for pos in range(0,len(list(text)),3):
				
				tmplist=[text[pos]^(a+97),text[pos+1]^(b+97),text[pos+2]^(c+97)]
				#print(tmplist)
				sum_tmp=sum([1 for i in tmplist if i >31 and i <127 ])
				#sum_tmp=3
				#print('%s\t%s\t%s\t:\t%d\t%d\t%d\t:\t%s\t%d'%(a,b,c,text[pos],text[pos+1],text[pos+2],','.join(map(str,tmplist)),sum_tmp))
				message+=tmplist
			#message=message[1:2]
			#print(message)
			sum_let=sum([1 for i in message if i >31 and (i) <127])
			#print(sum_let)
			#print(','.join(map(chr,message[:10])))
			#print(len(message))
			if sum_let==len(message):
				if list(map(chr,message[:3]))==['A','n',' ']:
					print(*map(chr,message))
					print(sum(message))

#print((list(text)[0])^(list(text)[1]))