from helper import *

flag=0
num=0
sumN=0
while True:
    num+=1
    sumN+=num
    factorsN=factors(sumN)
    print(factorsN)
    print('%d'%(sumN))
    if len(factorsN)>500:break
