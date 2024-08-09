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

marks = float(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("Grade 'A'")

elif marks >=80 and marks < 90:
    print("Grade 'B'")
    
elif marks >= 60 and marks < 80:
    print("Grade C")

elif marks >= 40 and marks < 60:
    print("Grade 'D' ")

else: print("Grade 'E' ")
    

# WAP to make a calculator.


