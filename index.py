#Creating an empty my_list
my_list=[]
print(my_list)

#appending new elements to the my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#inserting a new item at the second position which is index 1
my_list.insert(1,15)
print(my_list)

#extending my list with a new range of items
my_list.extend([50, 60, 70])
print(my_list)

#deleting the last element from my_list
del (my_list [7])
print(my_list)

#sorting my_list in an ascending order
my_list.sort()
print(my_list)

#finding if the element 30 exists in my_list
print(my_list.index(30))

