with open('0067_triangle.txt') as f:
    t=[list(map(int,i.strip().split(' '))) for i in f.readlines()]
print(t[:5])

#def trisum(row,col):
    #print(row)
    #print(col)
    
tot=40#len(t)-1
ns=[]

maxCache=[]

for i in range(len(t)):
    temp=[]
    for j in range(len(t[i])):
        if i==0:
            msum=t[0][0]
            choice=[0,0] 
            temp.append(t[0][0])
        elif j==0: 
            choice=[0,0]
            temp.append(t[i][j]+maxCache[i-1][j])

        elif i==j: 
            choice=[-1,-1]
            temp.append(t[i][i]+maxCache[i-1][j-1])


        else: 
            choice = [-1,0]
            temp.append(t[i][j]+max(maxCache[i-1][j-1],maxCache[i-1][j]))
    maxCache.append(temp)

    print(max(maxCache[-1]))
'''
for i in range(tot):
        ns.append(trisum(tot,i))
        print('%d\tof\t%d\t%d'%(i+1,tot,max(ns)))
'''
