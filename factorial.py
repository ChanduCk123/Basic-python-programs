#let factorial of a nonnegative number n will be the product of all positive integers lessthan or equal to n.
n=int(input("enter the number: "))
fact=1
if(n<0):
	print("factorial does not exist for negative numbers")
elif(n==0):
	print("factorial of 0 is 1")
else:
	for i in range(1,n+1):
		fact=fact*i
	print(fact)
	
#################################
"""def factorial(n):
	result=1
	while n>=1:
		result=result*n
		n=n-1
	return result
n=int(input("enter the number"))
print(factorial(n))   """
#res=factorial(n)
#print(res)
#or 
#print(factorial(3))
"""
def fact(n):
	if n==0:
		return 1
	else:
		return n*fact(n-1)
n=int(input("enter the num"))
print(fact(n))
"""
##################
"""def factorial(n):
	result=1
	while n>=1:
		result=result*n
		n=n-1
	return result
for i in range(1,10):
	print("the factorial of ", i , "is", factorial(i))
"""
)

