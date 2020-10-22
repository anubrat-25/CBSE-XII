#Bubble Sort

l=[3,5,7,2,1,4,9,8,6]

for i in range(0,len(l)):
    for j in range(0,len(l)-i-1):
        
        if l[j] > l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
            
print(l)