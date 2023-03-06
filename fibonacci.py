#fibonacci numbers,it is the series of the integr nums ,and here each num, except 1st 2 nums are the sum of previous 2 nums ex:0,1,1,2,3,5,8
"""n=int(input("enter the how many nums do you want is this series: "))
a=0
b=1
for i in range(n):     
	print(a,end=" ")	
	temp=a   	
	a=b  		
	b=temp+b  """  	

######
def fib(n):
	a,b=0,1
	for i in range(n):
		print(a,end=", ")
		a,b=b,a+b
n=int(input("enter how many lines do u want"))
fib(n)

#using recursion
"""def fib(n):
	assert int(n)==n and n>=0, "pls enter +ve int"
	if n in [0,1]: # or if n<=1,return n
		return n
	else:
		return fib(n-1)+fib(n-2)
n=5
for i in range(n):
	print(fib(i),end=" ")  """
#0 1 1 2 3

#fibonacci
"""
a=[0,1]
[a.append(a[-2]+a[-1])for i in range(5)]
print(a) #[0, 1, 1, 2, 3, 5, 8] """

#wap for nth fibonacci number
"""def fib(n):
	if n<=0:
		print("incorrect input")
	elif n==1:
		return 0
	elif n==2:
		return 1
	else:
		return fib(n-1)+fib(n-2)
print(fib(10)) #34"""
#or
#k=10
#for i in range(1,k+1):
#	print(fib(i),end=" ") #0 1 1 2 3 5 8 13 21 34

#check if the given num is fibonacci or not
"""n=10
l=[]
a=0
b=1
for i in range(n):
	l.append(a)
	temp=a
	a=b
	b=temp+b
print(l)
k=int(input("check the the num is fib or not: "))
if k in l:
	print("yes")
else:
	print("no")"""
