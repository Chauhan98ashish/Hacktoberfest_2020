print("*****Square Root By Newton's Method*****")
x=int(input("Enter the number::>>"))
r=x
a=10**(-10)
while abs(x-r*r)>a:
    r=(r+x/r)/2
    print(r)
r=round(r,3)
print("Square root of {} is {}".format(x,r))
