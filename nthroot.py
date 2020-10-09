def nth(bs,expo):
	expo= 1 / expo
	x= bs ** expo
	return x

p=int(input("Enter value of base:"))
q=int(input("Enter value of exponent:"))

print(nth(p,q))