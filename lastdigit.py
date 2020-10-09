def mindg(x,y):
	i= x % 10
	j= y % 10
	if i > j:
		return x
	elif i == j:
		print()
	else:
		return y

a=int(input("Enter 1st No.:"))
b=int(input("Enter 2nd No.:"))

print(mindg(a,b))