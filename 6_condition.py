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
    