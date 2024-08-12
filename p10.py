from helper import *

cumsum=0
for i in range(1,2000001):
    if isPrime2(i): cumsum+=i

print(cumsum)
