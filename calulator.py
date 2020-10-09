def sum(x,y):
	print(x+y)

def sub(x,y):
	print(x-y)

def mult(x,y):
	print(x*y)

def div(x,y):
	print(x/y)

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))


ch=int(input("Enter choice number (1.Add/2.Subtract/3.Multipy/4.Divide):"))

if ch==1:
	sum(a,b)
elif ch==2:
	sub(a,b)
elif ch==3:
	mult(a,b)
elif ch==4:
	div(a,b)
else:
	print("Invalid choice!")
	