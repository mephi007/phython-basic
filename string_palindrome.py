def fact(n):
	if n==1:
		return n
	else:
		return n*fact(n-1)

num=input("enter a number: ")
if num<0:
	print "factorial of negative values does not exist"
elif num==0:
	print "factorial is 1"
else:
	print "factorial is ", num , "is" , fact(num)