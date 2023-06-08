lst=['a','b','c','d','e']
i=0
with open('christmasCards/employees.txt','r') as names:
    for i in 0,1,2,3,4:
        lst[i]=(names.readline())
    
    names.close()
    
for i in 0,1,2,3,4:
        print(lst[i])
        
