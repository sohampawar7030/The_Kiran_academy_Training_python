List1  = [1, 2, 3, 4, 5, 6, 7, 8]
Set1  = {5, 6, 7, 8, 9, 10}
# # # Tasks:
# # 1.	Remove duplicates from my_list using a set and print the result.
# list1=set(List1)
# print(list1)
# 2.	Combine my_list and my_set into one collection (without duplicates), preserving the order of the list elements. Print the combined collection.
# List1  = [1, 2, 3, 4, 5, 6, 7, 8]
# Set1  = {5, 6, 7, 8, 9, 10}
# print('combine set :',Set1.update(List1))
# print(Set1)
# 3.	Find the intersection between my_list and my_set. Print the result.
# List1  = [1, 2, 3, 4, 5, 6, 7, 8]
# Set1  = {5, 6, 7, 8, 9, 10}
# Set2=set(List1)
# print(Set1 & Set2) 
# 4.	Find the union of my_list and my_set. Print the result.
# List1  = [1, 2, 3, 4, 5, 6, 7, 8]
# Set1  = {5, 6, 7, 8, 9, 10}
# print("union of Two set :",Set1.union(List1))
# # 5.	Remove the last element from my_list using the pop() method and print the modified list.
# print("Remove the Element at end ",List1.pop())
# print(List1)
# 6.	Remove and return an arbitrary element from my_set using the pop() method, and print the updated set.
# List1  = [1, 2, 3, 4, 5, 6, 7, 8]
# Set1  = {5, 6, 7, 8, 9, 10}
# Set1.pop()
# print(Set1)
# 7.	Check if all elements of my_list are present in my_set using the issubset() method. Print the result.
# List1  = [1, 2, 3, 4, 5, 6, 7, 8]
# Set1  = {5, 6, 7, 8, 9, 10}
# set2=set(List1)
# print(set2.issubset(Set1))
# # 8.	Add elements from my_list to my_set, but only the unique elements (no duplicates) using the update() method. Print the updated set.
# List =set(List1)
# print(Set1.update(List))
# print(Set1)
# List1.extend(Set1)
# print(List1)

# 9.	Remove the element at index 2 from my_list using the pop() method and print the modified list.
# List1  = [1, 2, 3, 4, 5, 6, 7, 8]
# Set1  = {5, 6, 7, 8, 9, 10}

# List1.pop(2)
# print(List1)
# 10.	Check the difference between my_set and my_list, i.e., elements in the set but not in the list, using the difference() method. Print the result.
# List1  = [1, 2, 3, 4, 5, 6, 7, 8]
# Set1  = {5, 6, 7, 8, 9, 10}
# print(Set1.difference(List1))

# 11.	Reverse the my_list using the reverse() method and print the result.
# List1  = [1, 2, 3, 4, 5, 6, 7, 8]
# print("Orignal List:",List1)
# List1.reverse()
# print(List1)
# 12.	Sort the my_list in ascending order using the sort() method and print the result.
# List1  = [1, 2, 3, 4, 5, 6, 7,1, 8]
# print(List1)
# List1.sort()
# print(List1)
# 13.	Clear all elements from my_set using the clear() method and print the empty set.
Set1  = {5, 6, 7, 8, 9, 10}
print(Set1)
Set1.clear()
print(Set1)
# 14.	Remove an element from my_set using the remove() method (with an existing element), and print the updated set.
Set1  = {5, 6, 7, 8, 9, 10}
Set1.remove(9)
print(Set1)
# 15.	Create a new set with elements that are not in my_list but are in my_set using the difference() method. Print this new set.
# Set1  = {5, 6, 7, 8, 9, 10}
# Set11 = {10,23,43,22,11,5,6,8}
# print(Set1.difference(Set11))
# 16.	Check if my_set and my_list are disjoint, meaning they have no common elements, using the isdisjoint() method. Print the result.
List1  = [1, 2, 3, 4, 5, 6, 7, 8]
Set1  = {5, 6, 7, 8, 9, 10}
print(Set1.isdisjoint(Set1))
# 17.	Count the occurrences of the number 3 in my_list using the count() method and print the result.
List1  = [1, 2, 3, 4, 5, 6, 7, 8]
print(List1.count(3))
# 18.	Append a new element 11 to my_list using the append() method, and print the updated list.
List1  = [1, 2, 3, 4, 5, 6, 7, 8]
List1.append(11)
print(List1)
# 19.	Insert the number 0 at the first position in my_list using the insert() method, and print the updated list.
List1  = [1, 2, 3, 4, 5, 6, 7, 8]
List1.insert(0,0)
print(List1)
# 20.	Copy the set to another set using the copy() method and print both sets.
Set1  = {5, 6, 7, 8, 9, 10}
Set3=Set1.copy()
print(Set1)
