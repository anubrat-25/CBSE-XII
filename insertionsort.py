#Insertion Sort

l=[3,5,7,2,1,4,9,8,6]

for i in range(1,len(l)):
    key=l[i]
    j=i-1

    while j >= 0 and key < l[j]:
        l[j+1]=l[j]
        j -= 1
    
    l[j+1] = key
    
print(l)
