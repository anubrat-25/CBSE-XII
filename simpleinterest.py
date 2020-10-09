def SI(p,n,r=10):
    Simple=(p*n*r)/100
    TA= p + Simple
    print(TA)

x=int(input("Enter Principle Amount:"))
y=int(input("Enter Time Duration:"))
#z=int(input("Enter Rate of Interest:"))

SI(x,y)