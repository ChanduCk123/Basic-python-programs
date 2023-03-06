n=int(input("Enter the year : "))
if(n%4==0) and (n%100 !=0):
	print("{0} is a leap year".format(n))
elif(n%100 ==0) and (n%400 ==0):
	print("{0} is a leap year".format(n))
else:
	print("{0} is not a leap year".format(n))

#########################

"""
def check(n):
	if(n%4==0):
		if(n%100==0):
			if(n%400==0):
				print("{0} is a leap year".format(n))
			else:
				print("{0} is not a leap year".format(n))
		else:
			print("{0} is not a leap year".format(n))
	else:
		print("{0} is not a leap year".format(n))
n=int(input("enter the year:"))
check(n)"""
