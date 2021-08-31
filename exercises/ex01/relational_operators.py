"""relational operators practice"""

x: str = (input("Left side: "))
y: str = (input("Right side: "))
s = int(x)
z = int(y)
print (x + " < " + y + " is ", bool(s<z))
print (x + " >= " + y + " is ", bool(s>=z))
print (x + " == " + y + " is ", bool(s==z))
print (x + " != " + y + " is ", bool(s!=z))

__author__ = "730214973"