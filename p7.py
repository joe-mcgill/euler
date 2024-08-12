primes=[]
from helper import *
x=1

while len(primes)<10001:
    if isPrime2(x):
        primes.append(x)
    x+=1

print(primes)
