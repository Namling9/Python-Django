'''
Conditions:

1) if
2) elif
3) else

'''

age = 18

if age>=18:
    print("you can vote")

else: 
    print("You can't vote")
    

# WAP which take input as age and print they are old or not.

age = int(input("Enter the age: "))

if(age >= 18 and age <50):
    
    print("You are an adult")

elif(age > 50 ):
    print("You are old")

else:
    print("You are a child")


data = "I am nonveg"

if "nonveg" in data:
    print("You are nonveg and you can eat meat")
    
else: 
    print("you are veg and you only eat vegetable")

#email validation

email = "name@gmail.com"

'''if "@" in email:
    print("your email is vaild email", email)

else: print("Your email is invalid email", email) '''

if "@" not in email:
    print("Wrong email", email)
    
else: print("Your email is valid", email)

