def seqLen(x):
    seq=[]
    seq.append(x)
    while x!=1:
        if x%2==0:
            x=x/2
            seq.append(x)
        else:
            x=3*x+1
            seq.append(x)
    return len(seq)

maxL=0
maxN=0
for i in range(1,1000000):
    temp=seqLen(i)
    if temp>maxL:
        maxL=temp
        maxN=i
    print('%d\t%d'%(maxN,maxL))
