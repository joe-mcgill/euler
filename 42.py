words=open('p042_words.txt').readlines()
print(max([len(i.strip('"')) for i in words[0].split(',')]))
words=[i.strip('"') for i in words[0].split(',')]
upperlim=14*26
tnums=[1]
n=1
while max(tnums)<upperlim:
	n+=1
	tnums.append(0.5*n*(n+1))
	print(tnums)

letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

twords=0

for i in words:
	scores=[(letters.find(j)+1) for j in i]
	if sum(scores) in tnums: twords+=1
print(twords)