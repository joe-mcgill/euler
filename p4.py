
from helper import *
ans=[]
for i in range(1,1000):
    for j in range(i,1000):
        prod=i*j
        if isPalindrome(prod):
            ans.append(prod)
            print('%d * %d = %d'%(i,j, prod))
print(max(ans))
