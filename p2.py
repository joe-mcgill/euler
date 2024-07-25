def fibseq(n):
    if (n==1):
        return 0
    elif (n==2):
        return 1
    else:
        return fibseq(n-1)+fibseq(n-2)
s=2
tempsum=0
flag=False
while flag==False:
    tempfib=fibseq(s)
    if tempfib>4000000: break
    if tempfib%2==0: tempsum+=tempfib
    s+=1
    print('%d\t%d\t%d'%(s,tempfib,tempsum))
