#checking type/casting float and int.
y=3.12
print(type(y),y)
z=int(y)
print(type(z),y)

x=3.0
print(type(x),x)
print(x)
y=int(x)
print(type(y),y)

x=-3.999
print(type(x),x)
y=int(x)
print(type(y),y)

#minutes to hour
minutes=360
hour=int(minutes/60)
print(minutes,"minutes to hours",hour)

#checking type/casting int and str.
x=int("2345")
print(type(x),x)
#checking type/casting int, float and str.
x=int("2345")
print(type(x),x)

x=int(17)
print(type(x),x)

#x=int("23 bottles")
#print(type(x),x)

x=float(17)
print(type(x),x)

y=float('123.45')
print(type(y),y)

x=str(17)
print(type(x),x)

y=str(123.45)
print(type(y),y)

#addition implicit line and explicit line

a=1+2+3+\
4+5+6+\
1+2
print("using more lines for addition :",a)
b=1+2+3+4+5+6+1+2
print("using one line for same addition :",b)
c=(1+2+3+
4+5+6+
1+2)
print("using bracket for addition: ",c)
