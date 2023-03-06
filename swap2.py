#Python program for swapping of a two numbers without using third variable
a=int(input("enter the N1:"))
b=int(input("enter the N2:"))
print("before swapping values are a=%d and b=%d"%(a,b))
a=a+b
b=a-b
a=a-b
print("after the swapping the values are a=%d and b=%d"%(a,b))
