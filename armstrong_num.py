#number of n digits which are equal to sum of nth power of its digits
"""num=int(input("enter the number: "))
temp=num
a=len(str(num))
s=0
while(temp>0):
	digit=temp%10
	s=s+(pow(digit,a))
	#s=s+(digit**a)
	temp=temp//10                      #370,153,1634
	
if(num==s):
	print(num," is a armstrong number")
else:
	print(num," is not armstrong number")
"""
##### or
"""n=153
temp=n 
l=len(str(n))
s=0
for i in str(n):
    s=s+int(i)**l
if s==temp:
    print("arms")
else:
    print("no")"""
########
#print armstrong nums the range btw 1 to 1000
"""for i in range(1,1000):
	a=len(str(i))
	s=0
	temp=i
	while temp>0:
		digit=temp%10
		s=s+digit**a
		temp=temp//10
	if i==s:
		print(i,end=" ")  """
#1 2 3 4 5 6 7 8 9 153 370 371 407 
