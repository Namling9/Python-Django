# Assignment (String)

# make example of about 10 pre defined function which can manipulation string with describe. 

a = "string is a collection of character"

print(a.upper()) #STRING IS A COLLECTION OF CHARACTER
print(a.lower()) # string is a collection of character
print(a.capitalize()) # String is a collection of character
print(a.title()) # String Is A Collection Of Character
print(a.swapcase()) #STRING IS A COLLECTION OF CHARACTER
print(a.find("is")) #7
print(a.replace("collection", "seqeunces")) # string is a seqeunces of character
print(a.count("c")) #4
print(",".join(a))
print(a.isspace())
print(a)

# WAP to replace data = " I love veg food " to " I love non-veg food"

data = "I love veg food"
print(data)
print(data.replace("veg", "non-veg"))

#split() - string

email = "namling@gmail.com"
split_data = email.split("@")
print(split_data)

second_part = split_data[1]


print(second_part.split("."))

# Strip()

name = "    My name is Namling"
print(name.strip())

#Condition

# WAP to take user input email and validate wether it is correct or not.

'''email = input("Enter your email: ")

if "@" in email:
    print(f"{email} is Valid Email")

else: print(f"{email} is not valid") '''

# WAP to take user input mark percentage and find their division

'''marks = float(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("Grade 'A'")

elif marks >=80 and marks < 90:
    print("Grade 'B'")
    
elif marks >= 60 and marks < 80:
    print("Grade C")

elif marks >= 40 and marks < 60:
    print("Grade 'D' ")

else: print("Grade 'E' ") '''
    

# WAP to make a calculator.
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

operator = input("Enter the operator: ")

if operator == "+":
    print("Sum of a and b : ", a+b)

elif operator == "-":
    print("Subtraction of a and b: ", a-b)
    
elif operator == "*":
    print("Multiplication of a and b : ", a*b)

elif operator == "/":
    print("Division of a and b: ", a/b)

elif operator == "%":
    print("Remainder of a and b : ", a%b)

else: print("Operator not available") '''

# WAP to find input number is prime or composite.
'''
num = int(input("Enter the number: "))

for i in range(2,num):
    if num % i == 0:
        print(num,"is a composite number")
        break


else: print(num,"is a prime number") 


# odd and even number 
'num = int(input("Enter the number: "))

if(num%2==0):
    print(f"{num} is an even number")

else: print(f"{num} is an odd number") '''

# Find lowest number among data = "822457313466823"
'''
data = "822457313466823"
lowest_num = 9

for i in data:
    
    i = int(i)
    if i < lowest_num:
        lowest_num = i
print("Lowest number : ",lowest_num) '''

#WAP to make a calculator, and choices is like y/n, if user press 'y' then he can add, subtration. 
#if user input 'n' then terminate calculating process
'''
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

while True: 
    user_in = input("Enter 'y' to calculate and Enter 'n' to terminate calculator : ")
    
    if(user_in == 'n'):
        break
    
    else: 
       operator = int(input("press '1' for addition and press '2' for subtraction : " ))
                            
       if(operator == 1):
           print("sum: ",a+b)
        
       elif(operator == 2): 
            print("subtration :", a-b) '''
       

# WAP to take 5 input number and find sum of all number.
'''
sum = 0
for i in range(5):
    n = int(input("Enter the number: "))
    sum += n
    
print(sum) '''