from helper import isPrime2

listP=[3,7,109,673]


def isPairPrime(x,y):
    if isPrime2(int(str(x)+str(y))) and isPrime2(int(str(y)+str(x))):
        return True
    else:
        return False

flag=0
newP=675

while flag==0:
    if isPrime2(newP):  
        
        tempList=list(map(isPairPrime,listP,[newP]*4)) 
        
        if sum(tempList)==4:
            print(newP)
            flag=1
    newP+=2
        
#print(sum(listP)+newP)
