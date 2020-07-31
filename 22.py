lets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

scores={lets[i]:(i+1) for i in range(26)}

names=open('p022_names.txt').readlines()

names=[i.strip('"') for i in names[0].split(',')]

names=sorted(names)

summ=0

def getname_score(name):
	name=[scores[l] for l in name]
	return(sum(name))

for i in range(len(names)):
	summ+=(i+1)*getname_score(names[i])

print(summ)