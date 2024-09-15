country = ["Nepal", "India", "USA"]

second_list = country

country.append("Japan")

print(second_list)


# copy the list

copied_list = country.copy()

country.append("Brazil")
print(copied_list) #['Nepal', 'India', 'USA', 'Japan']

print(second_list) #['Nepal', 'India', 'USA', 'Japan', 'Brazil']