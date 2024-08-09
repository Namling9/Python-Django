# give an example of each example
'''
1. Arthemetic Operator
2. Comparision operator
3. Logical Operator
4. Assignment Operator
5. Bitwise Operator
'''

# Arthemetic Operator
print("Arthemetic Operator: \n")
a = 5
b = 8

print("sum: ",a+b)
print("subtration: ",a-b)
print("multiply: ", a*b)
print("divide: ", a/b )
print("Remainder", a%b)
print("Square: ", a**b)

# Comparision operator
print("\n Comparision Operator: \n")
if(a>b):
    print("a is greater than b")

elif (a<b):
    print("a is smaller than b")

elif (a==b):
    print(" a and b is equal")

# Logical operator

print("\n Logical Operator: \n")

if (a >= 5 and b >=5): 
    
    print("a and b is greater than 5")
    
    if( a or b == 5):
        print("value of a or b is 5")
    else: print(" both a and b value is not 5 ")

else:
    print("a and b is not greater than 5")
        
x = False
print(not x) # true

# Assignment Operator
print("\n Assignment Operator: \n")
a = 5
a+= 5
print(a)

a-=5
print(a)

a*= 5
print(a)

a /=5
print(a)

a%=5
print(a)

print(8%2)

# bitwise operator

e = 5
f = 10

print(bin(e))
print(bin(f))
print(bin(e&f), e&f)
print(bin(e|f), e|f)
print(bin(e^f), e^f)