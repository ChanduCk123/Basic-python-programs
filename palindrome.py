#a palindrome is nothing but when a string or number which remains same when it is reversed
#m-1 normal
#using str(num) and reversed it
"""
num=int(input("enter the number: "))
temp=num
rev=0
while(num>0): 		     #323>0	    32>0     3>0  0>0false
	digit=num%10	     #323%10= 3 rem,32%10=2, 3
	rev=rev*10+digit     #0*10+3=3     ,3*10+2=32,323
	num=num//10          #323//10=32   ,32//10=3,0
if(temp==rev):
	print("{} is a paindrome".format(temp))
else:
	print("{} is not a palindrome".format(temp))
"""
# string palindrome
"""
n="radar"
s=""
for i in range(len(n)-1,-1,-1):
	s=s+n[i]
print(s)
if n==s:
	print("palin")
else:
	print("not paln")
	"""
##### string palindrome using built in function
"""
str=input("enter the string: ")
if(str==str[::-1]):
	print(str," is palindrome")
else:
	print(str," is not palindrome")
"""

