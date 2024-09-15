# for in data 
# WAP to calculate sum of all number available in data.
'''
data = "123456"
sum = 0
for i in data:
    
    sum += int(i)

print(f"sum of all number is :     {sum}") '''

# Find highest number from the give string
'''
data1 = "822345731396"
highest_num = 0

for i in data1:
    
    i = int(i)
    if(i>highest_num):
        highest_num = i

print(f"Highest number is : {highest_num}") '''
'''

for i in range(1,21):
    
    if i%2==0:
        print(f"Even : {i}")
    
    else : print(f"Odd : {i}")
'''
'''
num = 51
a=5
while num >a:
    
    num -= 1
    print(num)


# user input find int or string

a = input("Enter anything : ")

for i in a:
    
    if i.isdigit(): print("This is a digit.")
    
    
    else: print("This is a string") '''

# Control statement: 

# Break statement

for i in range(11):
    
    if i == 5:
        break # terminate loop
    
    print(i, end=" ") # 0 1 2 3 4
    
# continue statement

for i in range(11):
    
    if i == 5:
        continue # skip loop for now and continue loop 
    
    print(i, end=" ") # 0 1 2 3 4 6 7 8 9 10 

# Pass statement

for i in range(100):
    pass # skip the loop 


    
