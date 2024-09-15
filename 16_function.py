# Function

def design():
    print("This is design")
    print("****************")
    

# Types of function

# 1. Built-in function
# 2. Function with non parameter and non return type
# 3. Function with parameter and non return type
# 4. Function with non parameter and return type
# 5. Function with parameter and return type

# WAP to make a calculator using function

# class calculator:
#     def __init__(self,num1,num2):
        
#         self.num1 = num1
#         self.num2 = num2
    
#     def sum(self):
#         return self.num1+self.num2
    
#     def subtraction(self):
#         return self.num1-self.num2
    
#     def multiplication(self):
#         return self.num1*self.num2
    
#     def divide(self):
#         return self.num1/self.num2
    


# result = calculator(5,2)

# print("Sum :"result.sum())
# print(""result.subration())
# print(result.multiplication())
# print(result.divide())\
    
# def sum(num1,num2):
#         return num1+num2
    
# def subtraction(num1,num2):
#        return num1-num2
    
# def multiplication(num1,num2):
#        return num1*num2

# def divide(num1,num2):
#     return num1/num2


# print("Sum :",sum(5,4))
# print("subtraction: ",subtraction(5,4))
# print("Multiplication: ",multiplication(5,4))
# print("Divide: ", divide(5,4))

# def sum(num1,num2):
#         return num1+num2
    
# def subtraction(num1,num2):
#        return num1-num2
    
# def multiplication(num1,num2):
#        return num1*num2

# def divide(num1,num2):
#     return num1/num2

# num1 = int(input("Enter the 1st number: "))
# num2 = int(input("Enter the 2nd number: "))
# operator = (input("Enter the operator: "))

# if operator == "+":
#     print("Sum: ",sum(num1,num2))

# elif operator == "-":
#     print("Subtraction: ",subtraction(num1,num2))
    
# elif operator == "*":
#     print("Multiplication : ",multiplication(num1,num2))

# elif operator == "/":
#     print("Divide : ",divide(num1,num2))

# WAP to find given value is odd or even, Must include function in assignment.

def checkoddoreven(num):
    
    if num % 2 == 0:
        print(f"{num} is an even number")
    
    else: 
        print(f"{num} is an odd number")

number = int(input("Enter the number: "))
checkoddoreven(number)


