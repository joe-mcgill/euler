values={
	'1p': 1,
	'2p': 2,
	'5p': 5,
	'10p': 10,
	'20p':20,
	'50p':50,
	'100p': 100,
	'200p': 200
}
count=7
for a in range(1):
	for b in range(2):
		for c in range(4):
			if (a*200+b*100+c*50)>200:
				break
			for d in range(10):
				if (a*200+b*100+c*50+d*20)>200:
					break
				for e in range(20):
					if (a*200+b*100+c*50+d*20+e*10)>200:
						break
					#print('%d\t%d\t%d\t%d\t%d\t'%(a,b,c,d,e))
					for f in range(40):
						if (a*200+b*100+c*50+d*20+e*10+f*5)>200:
							break
						for g in range(100):
							if (a*200+b*100+c*50+d*20+e*10+f*5+g*2)>200:
								break
							for h in range(200):
								if (a*200+b*100+c*50+d*20+e*10+f*5+g*2+h)>200:
									break
							
								if (a*200+b*100+c*50+d*20+e*10+f*5+g*2+h)==200:
									count+=1
print(count)

