# List 

''' List is a collection which is ordered and changeable/mutable. allows to duplicate memebers'''

''' constructor : list_1 = list(("ram", "rita", ""sita))
    Square bracket: list_2 = ["ram", "sita", "rita"]
    
    '''
'''
l = ["January", "Feb", "March", "April", "May", "June", "July", "August", "september","Octuber","Nov","dec"]

print(l[0]) # January
print(l[-1]) # dec

# print(l[start : end : step])

print(l[0:3]) #['January', 'Feb', 'March']
print(l[0:8:2]) #['January', 'March', 'May', 'July']

print(l[5: : -2]) #['June', 'April', 'Feb'] '''

# add element in list

li = ["ram", "sita", "harry", "carry", "sorry"]

li.append("Jerry")
li.append("merry")

print(li) #['ram', 'sita', 'harry', 'carry', 'sorry', 'Jerry', 'merry']

# Insert element in list

li.insert(2, "laxmand")
print(li) #['ram', 'sita', 'laxmand', 'harry', 'carry', 'sorry', 'Jerry', 'merry']

# pop element in list

li.pop(2)
print(li) #['ram', 'sita', 'harry', 'carry', 'sorry', 'Jerry', 'merry']

# Remove element in list

li.remove("sorry")
print(li) #['ram', 'sita', 'harry', 'carry', 'Jerry', 'merry']


# len() - to find length of list

print(len(li))

# Replace in list

li[0] = "Krishna"
print(li) #['Krishna', 'sita', 'harry', 'carry', 'Jerry', 'merry']

# clear() - removes all elements from list

li.clear()
print(li)


# List in loop

subjects = ["math", "computer", "english", "nepali", "science"]

for i in subjects:
    print(i, end=", ") #math, computer, english, nepali, science, 
print()
# Access list item using while loop.

i = 0

while i < len(subjects):
    
    print(subjects[i], end = ", ") #math, computer, english, nepali, science,
    i+=1

print()
# Find highest digits from list = [1,23,423,4231,534,231,13,3456723,2313,43]

list = [1,23,423,4231,534,231,13,3456723,2313,43]
highest_num = 0
for i in list:
    
    if(i>highest_num):
        highest_num = i
print("Highest number in list: ", highest_num)    

# Print(max(list)) # 3456723

# Sort given list = [1,5,9,6,28,1203,4,23]
 
# list.sort()
#print(list) #[1, 13, 23, 43, 231, 423, 534, 2313, 4231, 3456723]
list = [23084,1,5,9,6,28,1203,4,23]
temp = 0
sorted_list = []


# Swap 
'''
a = 50
b = 80
print("Before sort : ", a, b)

if(a<b):
    temp = a # 50
    a = b # 80
    b = temp # 50
print("After sort", a, b) '''

# a,b=b,a # Swap 