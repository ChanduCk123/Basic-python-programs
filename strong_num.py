#145=1!+4!+5! sum of factorial of all digits of a num is equal to that num is the strong number

n=145
temp=n
s=0
while n>0:
    fact=1
    digit=n%10
    while digit>=1:
        fact=fact*digit
        digit=digit-1
    s=s+fact
    n=n//10
print(s)
if s==temp:
    print("strong  num")
else:
    print("not strong num")

