from tqdm import tqdm

pnums=[i*(3*i-1)/2 for i in range(1,5001)]

for i in tqdm(pnums):
	for j in pnums:
		if (i+ j) in pnums and abs(i-j) in pnums:
			print('%d\t%d\t%d'%(i,j,abs(i-j)))