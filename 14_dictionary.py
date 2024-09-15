# Dictionary

student = {
    'Name' : "namling Limbu",
    'Age' : 20,
    'Faculty': "BCA",
    'Class' : "Data science"
}

print(student)

print(student.keys())
print(student.values())
print(student.items())
print(student.pop('Class'))

new_student = student.copy()

print(new_student)

print(student.get('Name'))


subject = {
    'Maths' : 90,
    'Science' : 85,
    'English' : 95,
    'Computer': 99
}

for key in subject:
    
    #print(subject[key], end =" ") #90 85 95 99 
    print(f"Your mark in {key} subject is {subject[key]}")
    

# WAP a program to ask 5 subject and marks and print their pecentage and divsion.

dict = {}
total = 0
for i in range(5):
    
    subject = input(f"Enter the subject name: ")
    
    marks = int(input(f"Enter marks for {subject}: "))
    
    if 0 < marks and marks < 100:
        dict[subject] = marks
        total += marks

percentage = (total/500)*100

if percentage >= 90 and percentage <= 100:
            
    division = "Grade 'A'"
    print(division)

elif percentage >=80 and percentage < 90:
    division = "Grade 'B'"
    print(division)
    
elif percentage >= 60 and percentage < 80:
    division = "Grade 'C'"
    print(division)

elif percentage >= 40 and percentage < 60:
    division = "Grade 'D'"
    print(division)

else:  
    division = "Grade 'E'"
    print(division)
        
dict["Percentage"] = percentage
dict['Division'] = division
    
print(dict)

        



    
    
    