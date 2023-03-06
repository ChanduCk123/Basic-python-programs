#prime number is a natural number greater than 1,it is divisible by only 1 and itself and it is not divisible by any other number 
n=int(input("enter the num  "))
if n>1:
	for i in range(2,n):
		if(n%i)==0:
			print("it is not a prime num")
			break
	else:
		print(n,"is a prime number")
"""
start=int(input("enter the starting interval"))
end=int(input("enter the ending interval"))
for num in range(start,end+1):
	if num>1:
		for j in range(2,num):
			if(num%j)==0:
				break
		else:
			print(num,end="  ")"""
######################3
"""l=1
u = 100
for num in range(l,u+1):
	if num>1:
		if all(num % i !=0 for i in range(2,num)):
			print(num,end=" ")
"""
