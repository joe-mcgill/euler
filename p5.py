x=2

while True:
    
    flag=0
    x+=2
    if x%1000000==0:print(x)
    for i in [20,19,18,17,16,15,14,13,12,11]:
        
        if x%i!=0: 
            flag=1
            break
        
    if flag==0: 
        print(x)
        break
    


