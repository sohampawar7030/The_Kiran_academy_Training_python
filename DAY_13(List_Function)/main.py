List1=[10,20,30,40,50]
print(List1)
# append() Adds an element at the end of the list
print("use Append Method :",List1.append(100))
print(List1)
# clear() Removes all the elements from the list
List2=[10,20,30,40,50]

print("Use Clear Method :",List2.clear())
print(List2)
# copy() Returns a copy of the list
list3=List1.copy()
print(list3)
# count() Returns the number of elements with the specified value
list1=[1,2,3,4,5,7,9,0,1,2,3,5,7]
print(list1)
print("count Returns the number :",list1.count(1))
# extend() Add the elements of a list (or any iterable), to the end of the current list
list1=[1,2,4,5,7,8,54,22,6]
list2=[12,11,23,45,32,11]
print("extend:",list1.extend(list2))
print(list1)
# index() Returns the index of the first element with the specified value
print("index no :",list1.index(1))
# insert() Adds an element at the specified position
print(List1)
print("insert the value :",List1.insert(0,30))
print(List1)
# pop() Removes the element at the specified position
print(List1)
print("pop function Working:",List1.pop())
print(List1)
# remove() Removes the first item with the specified value
print(List1)
print("Remove Funtion Working:",List1.remove(40))
print(list1)
print("____________________________")
# reverse() Reverses the order of the list
print(List1)
print("Reverse Funtion :",list1.reverse())
print(List1)

# sort() Sorts the list
print(List1)
print("Sort Funtion :",list1.sort())
print(List1)