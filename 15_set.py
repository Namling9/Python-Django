# Set are faster than list

# set type conversion

f_list = [1,2,34,23,1,2]
f_set = set(f_list)
print(f_set)


data = ["apple", "ball", "apple"]
data_set = set(data)
print(data_set)

# add element in set

data_set.add("Cat")
print(data_set)

# Union Operation in set

people = {"jay", "ram", "sita"}
vampire = {"nogut", "cadts"}

population = people.union(vampire)
population_without_function = people|vampire
print(population) #{'sita', 'cadts', 'ram', 'jay', 'nogut'}
print(population_without_function) #{'sita', 'cadts', 'ram', 'jay', 'nogut'}

# Intersection

a = {1,2,3,42,10,12,11}
b = {2,102,123,12,3,11}

a_intersection_b = a.intersection(b)
print(a_intersection_b) #{11, 2, 3, 12}

a_intersection_b_without_function = a&b
print(a_intersection_b_without_function) #{11, 2, 3, 12}





